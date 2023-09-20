import pygame

from codes.common import consts, tools

class Fps(pygame.sprite.Sprite):
    def __init__(self):
        self.count = 15
        self.timer = 0
        self.index = 0
        self.img = tools.createLabel(consts.game_fps)


    def update(self):
        currentTime = pygame.time.get_ticks()

        self.index += 1
        if self.index % self.count == 0:
            interval = currentTime - self.timer
            self.timer = currentTime
            avg = float(interval) / self.count
            fps = 1000.0 / avg
            self.img = tools.createLabel(fps)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.img, self.img.get_rect())
