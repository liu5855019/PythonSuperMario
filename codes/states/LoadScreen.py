import pygame

from codes.common import consts


class LoadScreen:
    def __init__(self):
        self.done = False
        self.next = consts.strLevel1

    def update(self, surface, keys):
        pass

    def draw(self, surface):
        surface.fill(consts.colorBlue)

