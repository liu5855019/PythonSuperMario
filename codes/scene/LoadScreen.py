import pygame

from codes.scene import BaseScene
from codes.common import consts


class LoadScreen(BaseScene.BaseScene):

    def __init__(self):
        BaseScene.BaseScene.__init__(self)
        self.next = consts.strLevel1
        self.timer = 0


    def update(self, surface, keys):
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 2000:
            self.done = True
            self.timer = 0

    def draw(self, surface):
        surface.fill(consts.colorBlue)

