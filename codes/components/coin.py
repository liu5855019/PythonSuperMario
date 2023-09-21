import pygame
from codes.common import tools, consts, setup


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.frameIndex = 0

        self.loadFrames()
        self.image = self.frames[self.frameIndex]
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 58
        self.timer = 0

    def loadFrames(self):
        frame_rects = [(1, 160, 5, 8),
                       (9, 160, 5, 8),
                       (17, 160, 5, 8),
                       (9, 160, 5, 8)]
        itemObjects = setup.photos[consts.str_item_objects]
        for rect in frame_rects:
            self.frames.append(tools.getImage(itemObjects, *rect, (0, 0, 0), consts.bg_scale))

    def update(self) -> None:
        currentTime = pygame.time.get_ticks()
        frameIntervals = [375, 125, 125, 125]

        if self.timer == 0:
            self.timer = currentTime
        elif currentTime - self.timer > frameIntervals[self.frameIndex]:
            self.frameIndex += 1
            self.frameIndex %= 4
            self.timer = currentTime

        self.image = self.frames[self.frameIndex]
