import pygame.transform

from codes.scene import base_scene
from codes.common import consts, setup
from codes.components import info


class Level(base_scene.BaseScene):

    def __init__(self):
        base_scene.BaseScene.__init__(self)
        self.next = consts.str_level1
        self.info = info.Info(consts.str_level)
        self.setupBg()

    def setupBg(self):
        self.bg = setup.photos[consts.str_level1]
        rect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, (int(rect.width * consts.bg_scale),
                                                   int(rect.height * consts.bg_scale)))

    def update(self, surface, keys):
        self.info.update(surface)

    def draw(self, surface):
        surface.blit(self.bg, self.bg.get_rect())
        self.info.draw(surface)
