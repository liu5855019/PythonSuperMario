import pygame

from codes.common import consts, tools


class Fps(pygame.sprite.Sprite):

    def __init__(self):
        self.update_interval = consts.game_fps_update_interval
        self.timer = 0
        self.count = 0
        self.image = tools.createLabel(consts.game_fps)
        self.rect = self.image.get_rect()

    def update(self, surface: pygame.Surface):
        currentTime = pygame.time.get_ticks()
        interval = currentTime - self.timer

        self.count += 1
        if interval >= self.update_interval:
            avg = float(interval) / self.count
            fps = 1000.0 / avg
            strFps = '%.2f' % fps
            self.image = tools.createLabel(strFps)
            self.rect = self.image.get_rect()

            self.timer = currentTime
            self.count = 0

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

