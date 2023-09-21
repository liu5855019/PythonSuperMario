import pygame

from codes.scene import BaseScene
from codes.common import consts
from codes.components import Info


class LoadScreen(BaseScene.BaseScene):

    def __init__(self):
        BaseScene.BaseScene.__init__(self)
        self.next = consts.strLevel1
        self.timer = 0
        self.info = Info.Info(consts.strLoadScreen)


    def update(self, surface, keys):
        self.info.update(surface)
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 1000:
            self.done = True
            self.timer = 0

    def draw(self, surface):
        surface.fill(consts.colorBlack)
        self.info.draw(surface)

