import pygame
import random

import tools
import consts
import setup

class Game:

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self, state):
        while True:

            state.update(self.screen)

            # img = tools.getImage(setup.photos['mario_bros'], 145, 32, 16, 16, (0,0,0), random.randint(1, 5))
            # self.screen.blit(img, (300, 300))

            pygame.display.update()
            self.clock.tick(consts.game_fps)
        return
