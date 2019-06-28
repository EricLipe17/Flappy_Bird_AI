from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
import tensorflow as tf


class Brain:
    def __init__(self, learning_rate=1e-5):
        self.brain = Sequential()
        self.learning_rate = learning_rate

    def build_brain(self):
        self.brain.add(Dense(15, input_shape=(1, )))
        self.brain.add(Activation('sigmoid'))
        self.brain.add(Dense(10))
        self.brain.add(Activation('sigmoid'))
        self.brain.add(Dense(1))
        self.brain.add(Activation('sigmoid'))
        adam = Adam(lr=self.learning_rate)
        self.brain.compile(loss='mse', optimizer=adam)
        return self.brain

    def predict(self, inputs):
        output = self.brain.predict(inputs)
        return output



