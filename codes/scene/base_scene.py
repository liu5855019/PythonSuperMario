import pygame


class BaseScene:

    def __init__(self):
        self.done = False
        self.next = ''

    def update(self, surface: pygame.Surface, keys):
        pass

    def draw(self, surface: pygame.Surface):
        pass
