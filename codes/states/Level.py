import pygame

from codes.common import consts


class Level:
    def __init__(self):
        self.done = False
        self.next = None

    def update(self, surface, keys):
        pass

    def draw(self, surface):
        surface.fill(consts.colorWhite)

