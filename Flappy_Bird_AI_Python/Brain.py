from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
import tensorflow as tf
import numpy as np
import random


class Brain:
    def __init__(self, learning_rate=1e-5):
        tf.logging.set_verbosity(tf.logging.ERROR)
        self.brain = Sequential()
        self.learning_rate = learning_rate

    def build_brain(self):
        self.brain.add(Dense(5, input_shape=(1, )))
        self.brain.add(Activation('relu'))
        self.brain.add(Dense(1))
        self.brain.add(Activation('relu'))
        adam = Adam(lr=self.learning_rate)
        self.brain.compile(loss='mae', optimizer=adam)
        return self.brain

    def predict(self, inputs):
        output = self.brain.predict(inputs)
        return output

    def mutate(self, proba=0.1):
        weights = np.array(self.brain.get_weights())
        for array in weights:
            for val in array:
                if random.random() < proba:
                    (val + random.random()) / (1 + val)
        self.brain.set_weights(weights)
        return weights




