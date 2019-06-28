import pygame as pg
from Flappy_Bird_AI_Python import Brain
import numpy as np


class Bird:
    def __init__(self, window, neuro_evo=False):
        self.win = window
        self.x = 75
        self.y = self.win.get_height() // 2
        self.gravity = 0.6
        self.velocity = 0
        self.flap_force = 14

        self.bird_size = 20
        self.bird_img = pg.image.load("flappy_free.png")
        self.is_dead = False
        self.neuro_evo = neuro_evo
        self.score = 0
        self.fitness = 0
        if not self.neuro_evo:
            self.brain = None
        else:
            self.brain = Brain.Brain()
            self.brain.build_brain()

    # Calculates the bird's new position based on the "game physics."
    def update(self):
        self.score += 1
        if self.neuro_evo:
            if self.y >= self.win.get_height() - 23:
                # self.y = self.win.get_height() - 23
                self.velocity = 0
            elif self.y <= 2:
                # self.y = 2
                self.velocity = 0
            else:
                self.velocity += self.gravity
                self.velocity *= 0.95
                self.y += self.velocity
        else:
            if self.y >= self.win.get_height() - 23:
                self.y = self.win.get_height() - 23
                self.velocity = 0
                self.is_dead = True
            elif self.y <= 2:
                self.y = 2
                self.velocity = 0
                self.is_dead = True
            else:
                self.velocity += self.gravity
                self.velocity *= 0.95
                self.y += self.velocity

    # Applies the "flap force" to the bird and increases it's velocity.
    def flap(self):
        self.velocity -= self.flap_force

    # Checks if the bird is alive
    def check_health(self):
        return self.is_dead

    # Kills the bird
    def kill_bird(self):
        self.is_dead = True

    # Returns the rough 1-D pixel size of the bird.
    def get_bird_size(self):
        return self.bird_size

    # Writes the bird to the window.
    def show(self):
        self.win.blit(self.bird_img, (self.x, self.y))

    # Returns value of gravitational force.
    def get_gravity(self):
        return self.gravity

    # Sets the new value for the gravitational force.
    def set_gravity(self, new_gravity):
        self.gravity = new_gravity

    # This function decides whether or not to flap if neuro_evo is true.
    def decide(self, pipes):
        inputs = np.array([self.y / self.win.get_height(), pipes[0].get_top_lip() / self.win.get_height(),
                           pipes[0].get_bottom_lip() / self.win.get_height(), pipes[0].get_pipe_x() / self.win.get_width()])

        output = self.brain.predict(inputs)
        print(output[0])
        if output[0] >= 0.5:
            self.flap()













