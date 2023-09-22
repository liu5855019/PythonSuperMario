import pygame
import json

from codes.common import setup, consts, tools

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_datas()
        self.setup_states()
        self.setup_timers()
        self.setup_velocities()
        self.load_images()

    def load_datas(self):
        with open(consts.path_mario) as file:
            self.data = json.load(file)

        print(type(self.data))

    def setup_states(self):
        self.face_right = True
        self.dead = False
        self.big = False

    def setup_velocities(self):
        ###
        # 设置速度相关
        ###
        self.velocity_x = 0
        self.velocity_y = 0

    def setup_timers(self):
        self.timer_walk = 0  ### 步行时间
        self.time_transition = 0


    def load_images(self):
        sheet = setup.photos[consts.str_mario_bros]
        self.frames = []
        self.frames.append(tools.getImage(sheet, 178, 32, 12, 16, consts.color_black, consts.player_scale))

        self.frame_index = 0;
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self, surface: pygame.Surface, keys):
        if keys[pygame.K_RIGHT]:
            self.velocity_x = 5
        elif keys[pygame.K_LEFT]:
            self.velocity_x = -5
        else:
            self.velocity_x = 0

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
