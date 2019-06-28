import pygame
from Flappy_Bird_AI_Python import Bird, Pipe
import time
import math


class FlappyBird:
    def __init__(self, width=288, height=512, fps=60):
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
        self.bird = Bird.Bird(self.win, neuro_evo=False)
        self.pipes = list()
        self.bird_size = self.bird.get_bird_size()
        self.counter = 0
        self.background = pygame.image.load("flappy_background.png")
        self.initial_time = time.time()
        self.flapped = False
        self.bird.set_gravity(self.bird.get_gravity() * (60 / self.fps))

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
            if self.bird.y + 4 < temp_bottom_lip or self.bird.y + self.bird_size - 4 > temp_top_lip:
                if temp_left < self.bird.x + self.bird_size + 6 and self.bird.x < temp_right:
                    # If it is, kill the bird
                    self.bird.kill_bird()
                    return False

            if self.bird.x == pipe.get_pipe_x() + pipe.get_pipe_width() and not self.bird.check_health():
                self.pipes_passed += 1

            pipe.update()
        return True

    # Draw function that will draw the objects to screen.
    def draw(self):
        self.win.blit(self.background, (0, 0))
        self.win.blit(self.score_board, (0, 0))
        self.win.blit(self.pipe_score_board, (0, 20))
        self.bird.show()
        self.bird.update()

        self.draw_pipe_check_collision_increment_score()
        pygame.display.update()

    # Simple function to keep track of the score and the amount of pipes passed.
    def calculate_score(self):
        self.score = time.time() - self.initial_time
        self.score_board = self.font.render("Score: " + str(math.floor(self.score)), True, (0, 0, 0))
        self.pipe_score_board = self.font.render("Pipes Passed: " + str(self.pipes_passed), True, (0, 0, 0))

    # This is where the game is run/drawn. Call this method when you only want to just play the Flappy Bird Game.
    def run(self):
        while not self.bird.check_health():
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bird.kill_bird()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()

            if (self.counter / 250).is_integer():
                self.pipes.append(Pipe.Pipe(self.win, 90))
            self.draw()
            self.calculate_score()
            self.counter += 1
        pygame.time.delay(1000)
        pygame.quit()

    # This function will be used in the Q-learning algorithm to return the state of the game.
    def frame_step(self, input_actions):
        pygame.event.pump()
        self.clock.tick(30)

        reward = 0.1
        terminal = False

        if sum(input_actions) != 1:
            raise ValueError("Multiple input actions!")

        # input_actions[0] == 1: do nothing
        # input_actions[1] == 1: flap the bird
        if input_actions[1] == 1:
            self.bird.flap()
            self.flapped = True

        if self.bird.is_dead:
            terminal = True
            print("\nBIRD DEAD\n")
            self.__init__()
            reward = -1

        if self.flapped:
            self.flapped = False

        # Draw background/scoreboard/bird
        self.win.blit(self.background, (0, 0))
        self.win.blit(self.score_board, (0, 0))
        self.win.blit(self.pipe_score_board, (0, 20))
        self.bird.show()
        self.bird.update()
        self.pipe_score_board = self.font.render("Pipes Passed: " + str(self.pipes_passed), True, (0, 0, 0))

        # Check crash/score/increment reward
        for pipe in self.pipes:
            if self.bird.x == pipe.get_pipe_x() + pipe.get_pipe_width() and not self.bird.check_health():
                reward = 1

        self.draw_pipe_check_collision_increment_score()

        if (self.counter / 250).is_integer():
            self.pipes.append(Pipe.Pipe(self.win, 90))
        self.counter += 1

        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.update()
        return image_data, reward, terminal

