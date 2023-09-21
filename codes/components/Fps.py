import pygame

from codes.common import consts, tools

class Fps(pygame.sprite.Sprite):
    def __init__(self):
        self.count = consts.game_fps_count
        self.timer = 0
        self.index = 0
        self.image = tools.createLabel(consts.game_fps)
        self.rect = self.image.get_rect()



    def update(self, surface: pygame.Surface):
        currentTime = pygame.time.get_ticks()

        self.index += 1
        if self.index % self.count == 0:
            interval = currentTime - self.timer
            self.timer = currentTime
            avg = float(interval) / self.count
            fps = 1000.0 / avg
            strFps = '%.2f'%fps
            self.image = tools.createLabel(strFps)
            self.rect = self.image.get_rect()


        self.draw(surface)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
