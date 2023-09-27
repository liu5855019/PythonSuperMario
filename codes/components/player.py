import enum

import pygame
import json

from codes.common import setup, consts, tools


class player_state(enum.Enum):
    stand = 1
    walk = 2
    jump = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_datas()
        self.setup_states()
        self.setup_timers()
        self.setup_speeds()
        self.load_images()

    def load_datas(self):
        with open(consts.path_mario) as file:
            self.datas = json.load(file)

    def setup_states(self):
        self.face_right = True
        self.dead = False
        self.big = False
        self.state: player_state = player_state.stand


    def setup_speeds(self):
        ###
        # 设置速度相关
        ###
        self.speed_x = 0
        self.speed_y = 0

        speed = self.datas["speed"]
        self.speed_max_walk = speed["max_walk_speed"]
        self.speed_max_ran = speed["max_run_speed"]
        self.speed_max_y = speed["max_y_velocity"]
        self.walk_accel = speed["walk_accel"]
        self.run_accel = speed["run_accel"]
        self.turn_accel = speed["turn_accel"]
        self.speed_jump = speed["jump_velocity"]
        self.gravity = consts.game_gravity

        self.speed_max_x = self.speed_max_walk
        self.accel_x = self.walk_accel

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
        self.current_time = pygame.time.get_ticks()

        self.handle_states(keys)


    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)



    def handle_states(self, keys):
        if self.state == player_state.stand:
            self.stand(keys)
        elif self.state == player_state.walk:
            self.walk(keys)
        elif self.state == player_state.jump:
            self.jump(keys)

        if self.face_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]


    def stand(self, keys):
        self.frame_index = 0
        self.speed_x = 0
        self.speed_y = 0
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            self.state = player_state.walk
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            self.state = player_state.walk




    def walk(self, keys):
        self.speed_max_x = self.speed_max_walk
        self.accel_x = self.walk_accel
        if self.current_time - self.timer_walk > 100:
            self.timer_walk = self.current_time
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
        if keys[pygame.K_RIGHT]:
            self.face_right = True
            if self.speed_x <0:
                self.frame_index = 5
                self.accel_x = self.turn_accel
            self.speed_x = self.count_speed(self.speed_x, self.accel_x, self.speed_max_x, self.face_right)
        elif keys[pygame.K_LEFT]:
            self.face_right = False
            if self.speed_x > 0:
                self.frame_index = 5
                self.accel_x = self.turn_accel
            self.speed_x = self.count_speed(self.speed_x, self.accel_x, self.speed_max_x, self.face_right)
        else:
            if self.speed_x > 0:
                self.speed_x -= self.accel_x
                if self.speed_x < 0:
                    self.speed_x = 0
                    self.state = player_state.stand
            elif self.speed_x < 0:
                self.speed_x += self.accel_x
                if self.speed_x > 0:
                    self.speed_x = 0
                    self.state = player_state.stand
            else:
                self.state = player_state.stand


    def jump(self, keys):
        pass

    def count_speed(self, speed, accel, speed_max, is_right = True):
        if is_right:
            return min(speed + accel, speed_max)
        else:
            return max(speed - accel, -speed_max)