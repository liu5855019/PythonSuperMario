import pygame.transform
import json

from codes.scene import base_scene
from codes.common import consts, setup
from codes.components import info, player


class Level(base_scene.BaseScene):

    def __init__(self):
        base_scene.BaseScene.__init__(self)
        self.next = consts.str_level1
        self.info = info.Info(consts.str_level)
        self.load_level_datas()
        self.setupBg()
        self.setup_start_position()
        self.setup_player()

    def load_level_datas(self):
        with open(consts.path_level1) as file:
            self.datas = json.load(file)

    def setupBg(self):
        self.bg = setup.photos[consts.str_level1]
        rect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, (int(rect.width * consts.bg_scale),
                                                   int(rect.height * consts.bg_scale)))
        bg_rect = self.bg.get_rect()
        self.game_window_rect = setup.screen.get_rect()
        self.game_ground = pygame.Surface((bg_rect.width, bg_rect.height))

    def setup_start_position(self):
        map0 = self.datas['maps'][0]
        self.start_x = map0['start_x']
        self.end_x = map0['end_x']
        self.player_x = map0['player_x']
        self.player_y = map0['player_y']

    def setup_player(self):
        self.player = player.Player(consts.str_mario)
        self.player.rect.x = self.game_window_rect.x + self.player_x
        self.player.rect.bottom = self.player_y

    def update_player_position(self):
        self.player.rect.x += self.player.speed_x
        if self.player.rect.x < self.start_x:
            self.player.rect.x = self.start_x
        elif self.player.rect.x < self.game_window_rect.x:
            self.player.rect.x = self.game_window_rect.x
        elif self.player.rect.x > self.end_x - self.player.rect.width:
            self.player.rect.x = self.end_x - self.player.rect.width

        self.player.rect.y += self.player.speed_y

    def update_game_window(self):
        position = self.game_window_rect.x + self.game_window_rect.width / 3.0
        if (self.player.speed_x > 0
                and self.player.rect.centerx > position):
            self.game_window_rect.x += self.player.speed_x
            if self.game_window_rect.x > self.end_x - consts.screen_w:
                self.game_window_rect.x = self.end_x - consts.screen_w

    def update(self, surface, keys):
        self.info.update(surface)
        self.player.update(surface, keys)
        self.update_player_position()
        self.update_game_window()

    def draw(self, surface):
        self.game_ground.blit(self.bg, self.game_window_rect, self.game_window_rect)
        self.player.draw(self.game_ground)
        surface.blit(self.game_ground, (0, 0), self.game_window_rect)
        self.info.draw(surface)
