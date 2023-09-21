import pygame

from codes.common import tools, setup, consts
from codes.components import info
from codes.scene import base_scene


class MainMenu(base_scene.BaseScene):
    def __init__(self):
        base_scene.BaseScene.__init__(self)
        self.cursor = pygame.sprite.Sprite()
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info(consts.str_main_menu)
        self.done = False
        self.next = consts.str_load_screen
        self.cursor.state = '1P'

    def setup_background(self):
        self.bg = setup.photos[consts.str_level1]
        bgRect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, tools.reSize(bgRect.width, bgRect.height, consts.bg_scale))
        self.caption = tools.getImage(setup.photos['title_screen'], 1, 60, 176, 88, (255, 0, 220), consts.bg_scale)

    def setup_player(self):
        self.player = tools.getImage(setup.photos[consts.str_mario_bros], 178, 32, 12, 16, (0, 0, 0), consts.player_scale)

    def setup_cursor(self):
        self.cursor.image = tools.getImage(setup.photos[consts.str_item_objects], 24, 160, 8, 8, (0, 0, 0),
                                           consts.player_scale)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (200, 360)
        self.cursor.rect = rect

    def updateCursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = '1P'
            self.cursor.rect.y = 360
        elif keys[pygame.K_DOWN]:
            self.cursor.state = '2p'
            self.cursor.rect.y = 405
        elif keys[pygame.K_RETURN]:
            if self.cursor.state == '1P':
                self.done = True
            elif self.cursor.state == '2P':
                self.done = True

    def update(self, surface, keys):
        self.updateCursor(keys)
        self.info.update(surface)

    def draw(self, surface):
        surface.blit(self.bg, surface.get_rect())
        surface.blit(self.caption, (170, 100))
        surface.blit(self.player, (110, 490))
        surface.blit(self.cursor.image, self.cursor.rect)

        self.info.draw(surface)
