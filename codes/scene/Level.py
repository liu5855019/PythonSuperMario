import pygame.transform

from codes.scene import BaseScene
from codes.common import consts, setup
from codes.components import Info


class Level(BaseScene.BaseScene):

    def __init__(self):
        BaseScene.BaseScene.__init__(self)
        self.next = consts.strLevel1
        self.info = Info.Info(consts.strLevel)
        self.setupBg()

    def setupBg(self):
        self.bg = setup.photos[consts.strLevel1]
        rect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, (int(rect.width * consts.bg_scale),
                                                   int(rect.height * consts.bg_scale)))

    def update(self, surface, keys):
        self.info.update(surface)

    def draw(self, surface):
        surface.blit(self.bg, self.bg.get_rect())
        self.info.draw(surface)
