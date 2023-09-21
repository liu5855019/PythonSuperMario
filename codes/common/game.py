import pygame
import sys

import consts
from codes.scene import base_scene
from codes.components import fps


class Game:

    def __init__(self, sceneDict, startScene):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.sceneDict = sceneDict
        self.scene: base_scene.BaseScene = self.sceneDict[startScene]
        self.fps = fps.Fps()

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()

            self.update()

            self.fps.update(self.screen)

            pygame.display.update()
            self.clock.tick(consts.game_fps)
        return

    def update(self):
        if self.scene.done:
            self.scene.done = False
            self.scene = self.sceneDict[self.scene.next]

        self.scene.update(self.screen, self.keys)
        self.scene.draw(self.screen)
