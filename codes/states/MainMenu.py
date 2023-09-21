import pygame

from codes.common import tools, setup, consts
from codes.components import Info


class MainMenu():
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = Info.Info(consts.strMainMenu)

    def setup_background(self):
        self.bg = setup.photos[consts.strLevel1]
        bgRect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, tools.reSize(bgRect.width, bgRect.height, consts.bg_scale) )
        self.caption = tools.getImage(setup.photos['title_screen'], 1, 60, 176, 88, (255,0,220), consts.bg_scale)

    def setup_player(self):
        self.player = tools.getImage(setup.photos[consts.strMarioBros], 178,32, 12, 16, (0,0,0), consts.player_scale)

    def setup_cursor(self):
        self.cursor = tools.getImage(setup.photos[consts.strItemObjects], 24, 160, 8, 8, (0,0,0), consts.player_scale)

    def update(self, surface: pygame.Surface):
        # surface.fill(tools.randomColor)
        surface.blit(self.bg, surface.get_rect())
        surface.blit(self.caption, (170, 100))
        surface.blit(self.player, (110, 490))
        surface.blit(self.cursor, (220,360))

        self.info.update(surface)
