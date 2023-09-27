import enum

import pygame
import json

from codes.common import setup, consts, tools


class player_state(enum.Enum):
    walk=1
    jump=2

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
            self.datas = json.load(file)

    def setup_states(self):
        self.face_right = True
        self.dead = False
        self.big = False
        self.state = player_state.walk


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
        # self.frames = []
        # self.frames.append(tools.getImage(sheet, 178, 32, 12, 16, consts.color_black, consts.player_scale))

        self.right_small_frames = []
        self.right_big_frames = []
        self.right_fire_frames = []
        self.left_small_frames = []
        self.left_big_frames = []
        self.left_fire_frames = []

        self.small_frames = [self.right_small_frames, self.left_small_frames]
        self.big_frames = [self.right_big_frames, self.left_big_frames]
        self.fire_frames = [self.right_fire_frames, self.left_fire_frames]

        self.right_frames = self.right_small_frames
        self.left_frames = self.left_small_frames

        sheet = setup.photos[consts.str_mario_bros]
        frame_rect_dict: dict = self.datas[consts.str_image_frames]
        for key, rects in frame_rect_dict.items():
            for rect in rects:
                right_image = tools.getImage(sheet,
                                             rect["x"],
                                             rect["y"],
                                             rect["width"],
                                             rect["height"],
                                             consts.color_black,
                                             consts.player_scale)
                left_image = pygame.transform.flip(right_image, True, False)

                if key == consts.str_right_small_normal:
                    self.right_small_frames.append(right_image)
                    self.left_small_frames.append(left_image)
                elif key == consts.str_right_big_normal:
                    self.right_big_frames.append(right_image)
                    self.left_big_frames.append(left_image)
                elif key == consts.str_right_big_fire:
                    self.right_fire_frames.append(right_image)
                    self.left_fire_frames.append(left_image)

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self, surface: pygame.Surface, keys):
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.velocity_x = 5
            self.velocity_y = 0
            self.state = player_state.walk
        elif keys[pygame.K_LEFT]:
            self.velocity_x = -5
            self.velocity_y = 0
            self.state = player_state.walk
        elif keys[pygame.K_SPACE]:
            self.velocity_x = 0
            self.velocity_y = -5
            self.state = player_state.jump

        if self.state == player_state.walk:
            if current_time - self.timer_walk > 100:
                self.timer_walk = current_time
                self.frame_index += 1
                self.frame_index %= 4

        if self.state == player_state.jump:
            self.frame_index = 4

        self.image = self.frames[self.frame_index]

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
