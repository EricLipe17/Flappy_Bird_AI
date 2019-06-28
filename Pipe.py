import pygame as pg
import random


class Pipe:
    def __init__(self, window, gap_in):
        self.win = window
        self.x = self.win.get_width()

        self.min_height = self.win.get_height() / 8
        self.rect_height = self.win.get_height() / 2
        self.pipe_width = 48

        self.free_space = gap_in
        self.speed = 1
        self.rand_length = random.randint(150, self.rect_height)

        self.top_lip = self.min_height + self.rand_length
        self.bottom_lip = self.top_lip - self.free_space

        self.up_pipe = pg.image.load("up_pipe.png")
        self.down_pipe = pg.image.load("down_pipe.png")

    # Writes the pipe to the window.
    def show(self):
        self.win.blit(self.down_pipe, (self.x, self.bottom_lip - 320))
        self.win.blit(self.up_pipe, (self.x, self.top_lip))

    # Updates the pipe's current position by incrementing its x-position.
    def update(self):
        self.x -= self.speed

    # Sets the pipes speed.
    def set_speed(self, new_speed):
        self.speed = new_speed

    # Returns the y-position of the lip for the "up pipe."
    def get_top_lip(self):
        return self.top_lip

    # Returns the y-position of the lip for the "down pipe."
    def get_bottom_lip(self):
        return self.bottom_lip

    # Determines if the pipe is off of the screen.
    def off_screen(self):
        if self.x + self.pipe_width < 0:
            return True
        return False

    # Returns the width of the pipe.
    def get_pipe_width(self):
        return self.pipe_width

    # Returns the x-position of the pipe.
    def get_pipe_x(self):
        return self.x


