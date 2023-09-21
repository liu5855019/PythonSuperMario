import pygame

from codes.scene import base_scene
from codes.common import consts
from codes.components import info


class LoadScreen(base_scene.BaseScene):

    def __init__(self):
        base_scene.BaseScene.__init__(self)
        self.next = consts.str_level1
        self.timer = 0
        self.info = info.Info(consts.str_load_screen)


    def update(self, surface, keys):
        self.info.update(surface)
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 1000:
            self.done = True
            self.timer = 0

    def draw(self, surface):
        surface.fill(consts.color_black)
        self.info.draw(surface)

