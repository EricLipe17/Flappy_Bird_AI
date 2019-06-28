from __future__ import print_function

import skimage as skimage
from skimage import transform, color, exposure
# from skimage.transform import rotate
# from skimage.viewer import ImageViewer

from Flappy_Bird_AI_Python import FlappyBird as game
import random
import numpy as np
from collections import deque

import json
# from keras.initializers import normal, identity
# from keras.models import model_from_json
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten
from keras.layers.convolutional import Convolution2D
from keras.optimizers import Adam
import tensorflow as tf

# Number of valid actions
actions = 2

# Decay rate for past observations
gamma = 0.99

# Timesteps to observe prior to training
observation = 3200.

# Frames over which to anneal epsilon
explore = 3000000.

# Final value of epsilon
final_epsilon = 0.0001

# Initial value of epsilon
initial_epsilon = 0.1

# Number of previous transitions to remember
replay_memory = 50000

# Size of batch
batch = 32
frame_per_action = 1
learning_rate = 1e-5

img_rows, img_cols = 80, 80
img_channels = 4


def build_model():
    model = Sequential()
    model.add(Convolution2D(32, (8, 8), strides=(4, 4), padding="same", input_shape=(img_rows, img_cols, img_channels)))  # 80*80*4
    model.add(Activation('relu'))
    model.add(Convolution2D(64, (4, 4), strides=(2, 2), padding="same"))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, (3, 3), strides=(1, 1), padding="same"))
    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dense(2))
    adam = Adam(lr=learning_rate)
    model.compile(loss='mse', optimizer=adam)
    return model


def train_network(model, args):
    game_state = game.FlappyBird(fps=30)

    # Using a deque to store observations in replay memory
    D = deque()

    # Get the first state by doing nothing a pre-process the image to 80x80x4
    do_nothing = np.zeros(actions)
    do_nothing[0] = 1
    x_t, r_0, terminal = game_state.frame_step(do_nothing)

    x_t = skimage.color.rgb2gray(x_t)
    x_t = skimage.transform.resize(x_t, (80, 80))
    x_t = skimage.exposure.rescale_intensity(x_t, out_range=(0, 255))

    x_t /= 255.

    s_t = np.stack((x_t, x_t, x_t, x_t), axis=2)

    # Reshape to match Keras' expectations
    s_t = s_t.reshape((1, s_t.shape[0], s_t.shape[1], s_t.shape[2]))

    if args == "Run":
        # We keep observe and never enter training mode.
        observe = 9999999999
        epsilon = final_epsilon
        print("Now we load weight.")
        model.load_weights("model.h5")
        adam = Adam(lr=learning_rate)
        model.compile(loss="mse", optimizer=adam)
        print("Weight load successful!")
    else:
        # Training mode
        observe = observation
        epsilon = initial_epsilon

    t = 0
    while True:
        loss = 0
        Q_sa = 0
        action_index = 0
        r_t = 0
        a_t = np.zeros([actions])

        # Choose an action via 'Epsilon Greedy Method'
        if t % frame_per_action == 0:
            if random.random() <= epsilon:
                print("------RANDOM ACTION------")
                action_index = random.randrange(actions)
                a_t[action_index] = 1
            else:
                # input a stack of 4 images, get the prediction
                q = model.predict(s_t)
                max_Q = np.argmax(q)
                action_index = max_Q
                a_t[max_Q] = 1

        # Reducing epsilon steadily
        if epsilon > final_epsilon and t > observe:
            epsilon -= (initial_epsilon - final_epsilon) / explore

        # Run selected action, observed next state and reward
        x_t1_colored, r_t, terminal = game_state.frame_step(a_t)

        x_t1 = skimage.color.rgb2gray(x_t1_colored)
        x_t1 = skimage.transform.resize(x_t1, (80, 80))
        x_t1 = skimage.exposure.rescale_intensity(x_t1, out_range=(0, 255))

        x_t1 /= 255.

        # 1x80x80x1
        x_t1 = x_t1.reshape((1, x_t1.shape[0], x_t1.shape[1], 1))

        s_t1 = np.append(x_t1, s_t[:, :, :, :3], axis=3)

        # Store the transition in D
        D.append((s_t, action_index, r_t, s_t1, terminal))
        if len(D) > replay_memory:
            D.popleft()

        # Only training if done observing
        if t > observe:
            # Sample batch to train on
            mini_batch = random.sample(D, batch)

            # Performing the experience replay
            state_t, action_t, reward_t, state_t1, terminal = zip(*mini_batch)
            state_t = np.concatenate(state_t)
            state_t1 = np.concatenate(state_t1)
            targets = model.predict(state_t)
            Q_sa = model.predict(state_t1)
            targets[range(batch), action_t] = reward_t + gamma * np.max(Q_sa, axis=1) * np.invert(terminal)

            loss += model.train_on_batch(state_t, targets)

            # Less optimal experience replay
            # inputs = np.zeros((batch, s_t.shape[1], s_t.shape[2], s_t.shape[3]))  # 32, 80, 80, 4
            # targets = np.zeros((inputs.shape[0], actions))  # 32, 2
            # for i in range(0, len(mini_batch)):
                # state_t = mini_batch[i][0]
                # action_t = mini_batch[i][1]  # This is action index
                # reward_t = mini_batch[i][2]
                # state_t1 = mini_batch[i][3]
                # terminal = mini_batch[i][4]
                #
                # # if terminated, only equals reward
                # inputs[i:i + 1] = state_t  # saved down s_t
                #
                # targets[i] = model.predict(state_t)  # Probability of hitting button
                # Q_sa = model.predict(state_t1)
                #
                # if terminal:
                #     targets[i, action_t] = reward_t
                # else:
                #     targets[i, action_t] = reward_t + gamma * np.max(Q_sa)
                #
                # loss += model.train_on_batch(inputs, targets)

        s_t = s_t1
        t += 1

        # Save the networks progress every 10,000 iterations
        if t % 5000 == 0:
            print("Saving Model.")
            model.save_weights("model.h5", overwrite=True)
            with open("model.json", "w") as outfile:
                json.dump(model.to_json(), outfile)

        # Print info
        state = ""
        if t <= observe:
            state = "Observe"
        elif observe < t < observe + explore:
            state = "Explore"
        else:
            state = "Train"

        print("Timestep", t, "/ State", state,
              "/ Epsilon", epsilon, "/ Action", action_index, "/ Reward", r_t,
              "/ Q_Max", np.max(Q_sa), "/ Loss", loss)

    print("Episode Finished!")
    print("***********************")


def play_game(args):
    model = build_model()
    train_network(model, args)


def main(train=False):
    if train:
        play_game("Train")
    else:
        play_game("Run")


if __name__ == "__main__":
    config = tf.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.compat.v1.Session(config=config)
    from keras import backend as k_backend
    k_backend.set_session(sess)
    main(train=True)
