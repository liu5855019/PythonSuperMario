import pygame
import sys

import consts


class Game:

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()

    def run(self, state):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()

            state.update(self.screen, self.keys)

            # img = tools.getImage(setup.photos['mario_bros'], 145, 32, 16, 16, (0,0,0), random.randint(1, 5))
            # self.screen.blit(img, (300, 300))

            pygame.display.update()
            self.clock.tick(consts.game_fps)
        return
