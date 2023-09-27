import pygame.transform

from codes.scene import base_scene
from codes.common import consts, setup
from codes.components import info, player


class Level(base_scene.BaseScene):

    def __init__(self):
        base_scene.BaseScene.__init__(self)
        self.next = consts.str_level1
        self.info = info.Info(consts.str_level)
        self.setupBg()
        self.setup_player()

    def setupBg(self):
        self.bg = setup.photos[consts.str_level1]
        rect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, (int(rect.width * consts.bg_scale),
                                                   int(rect.height * consts.bg_scale)))

    def setup_player(self):
        self.player = player.Player(consts.str_mario)
        self.player.rect.x = 300
        self.player.rect.y = 490

    def update_player_position(self):
        self.player.rect.x += self.player.speed_x
        self.player.rect.y += self.player.speed_y

    def update(self, surface, keys):
        self.info.update(surface)
        self.player.update(surface, keys)
        self.update_player_position()




    def draw(self, surface):
        surface.blit(self.bg, self.bg.get_rect())
        self.info.draw(surface)
        self.player.draw(surface)
