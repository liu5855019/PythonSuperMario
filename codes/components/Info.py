import pygame

from codes.common import consts
from codes.components import Coin, Fps

pygame.font.init()


class Info:
    def __init__(self, state):
        self.state = state
        self.infoLabels = []
        self.stateLabels = []

        self.createStateLabels()
        self.createInfoLabels()
        self.coin = Coin.Coin()
        self.fps = Fps.Fps()


    def createStateLabels(self):
        if self.state == consts.strMainMenu:
            self.stateLabels.append((self.createLabel('1 PLAYER GAME'), (272, 360)))
            self.stateLabels.append((self.createLabel('2 PLAYER GAME'), (272, 405)))
            self.stateLabels.append((self.createLabel('TOP - '), (290, 465)))
            self.stateLabels.append((self.createLabel('000000'), (400, 465)))

    def createInfoLabels(self):
        self.infoLabels.append((self.createLabel('MARIO'), (75, 30)))
        self.infoLabels.append((self.createLabel('WORLD'), (450, 30)))
        self.infoLabels.append((self.createLabel('TIME'), (625, 30)))
        self.infoLabels.append((self.createLabel('000000'), (75, 55)))
        self.infoLabels.append((self.createLabel('x00'), (300, 55)))
        self.infoLabels.append((self.createLabel('1 - 1'), (480, 55)))

    def createLabel(self, label, fontSize=40, wScale=1.25, hScale=1):
        font = pygame.font.SysFont(consts.fontName, fontSize)
        labelImg = font.render(label, 1, consts.colorWhite)
        rect = labelImg.get_rect()
        labelImg = pygame.transform.scale(labelImg, (int(rect.width * wScale), int(rect.height * hScale)))
        return labelImg

    def update(self):
        self.coin.update()
        self.fps.update()

    def draw(self, surface: pygame.Surface):
        for label in self.stateLabels:
            surface.blit(label[0], label[1])

        for label in self.infoLabels:
            surface.blit(label[0], label[1])

        surface.blit(self.coin.image, self.coin.rect)
        self.fps.draw(surface)
