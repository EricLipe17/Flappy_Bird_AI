import pygame
from Flappy_Bird_AI_Python import Bird, Pipe
import math
import time
import random
import numpy as np


class FlappyBirdNeuroEvo:
    def __init__(self, num_agents=50, width=288, height=512, fps=60):
        pygame.init()
        pygame.font.init()
        self.win = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.pipes_passed = 0
        self.score = 0
        self.font = pygame.font.SysFont("Times New Roman", 20)
        self.score_board = self.font.render("Score: " + str(self.score), True, (0, 0, 0))
        self.pipe_score_board = self.font.render("Pipes Passed: " + str(self.pipes_passed), True, (0, 0, 0))
        self.background = pygame.image.load("flappy_background.png")

        self.pipes = list()
        self.birds = list()
        self.dead_birds = list()
        self.num_agents = num_agents
        for i in range(self.num_agents):
            self.birds.append(Bird.Bird(self.win, neuro_evo=True))
            self.birds[i].set_gravity(self.birds[i].get_gravity() * (60 / self.fps))
        self.bird_size = self.birds[0].get_bird_size()
        self.counter = 0
        self.initial_time = time.time()

    def draw_pipe_check_collision_increment_score(self):
        for pipe in self.pipes:
            if pipe.off_screen():
                self.pipes.remove(pipe)
            else:
                pipe.set_speed(60 / self.fps)
                pipe.show()

            # Create temp variables for each pipe set to check vs bird position.
            temp_left = pipe.get_pipe_x()
            temp_right = temp_left + pipe.get_pipe_width()
            temp_top_lip = pipe.get_top_lip()
            temp_bottom_lip = pipe.get_bottom_lip()
            # Check if the bird is in a pipe
            for bird in self.birds:
                if bird.y + 4 < temp_bottom_lip or bird.y + self.bird_size - 4 > temp_top_lip:
                    if temp_left < bird.x + self.bird_size + 6 and bird.x < temp_right:
                        # If it is, remove the bird
                        bird.velocity = 0
                        self.dead_birds.append(bird)
                        self.birds.remove(bird)
                        return False

                if bird.x == pipe.get_pipe_x() + pipe.get_pipe_width() and not bird.check_health():
                    self.pipes_passed += 1

            pipe.update()
        return True

    # Draw function that will draw the objects to screen.
    def draw(self):
        self.win.blit(self.background, (0, 0))
        self.win.blit(self.score_board, (0, 0))
        self.win.blit(self.pipe_score_board, (0, 20))
        for bird in self.birds:
            bird.decide(self.pipes)
            bird.show()
            bird.update()

        self.draw_pipe_check_collision_increment_score()
        pygame.display.update()

    # Simple function to keep track of the score and the amount of pipes passed.
    def calculate_score(self):
        self.score = time.time() - self.initial_time
        self.score_board = self.font.render("Score: " + str(math.floor(self.score)), True, (0, 0, 0))
        self.pipe_score_board = self.font.render("Pipes Passed: " + str(self.pipes_passed), True, (0, 0, 0))

    # Linearly assigns a fitness value to each of the birds.
    def calculate_fitness(self):
        score_sum = 0
        for bird in self.birds:
            score_sum += bird.score

        for bird in self.birds:
            bird.fitness = bird.score / score_sum

    def pick_bird(self):
        print(len(self.dead_birds))
        child = self.dead_birds[np.random.randint(low=0, high=self.num_agents)]

        child.brain.mutate(0.1)
        return child

    # Creates the next generation of birds.
    def next_gen(self):
        self.calculate_fitness()
        for i in range(self.num_agents):
            self.birds.append(self.pick_bird())

    # This is where the game is run/drawn.
    def run(self):
        # self.pipes.append(Pipe.Pipe(self.win, 90))
        quit_game = False
        while not quit_game:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True

            if (self.counter / 250).is_integer():
                self.pipes.append(Pipe.Pipe(self.win, 90))

            self.draw()
            self.calculate_score()
            if len(self.birds) == 0:
                self.next_gen()
                self.dead_birds.clear()
                self.pipes.clear()
                self.counter = -1

            self.counter += 1
        pygame.time.delay(1000)
        pygame.quit()


evo = FlappyBirdNeuroEvo(num_agents=50, fps=60)

evo.run()
