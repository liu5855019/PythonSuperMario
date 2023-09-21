import pygame

from codes.common import consts, tools, setup
from codes.components import coin

pygame.font.init()


class Info:
    def __init__(self, state):
        self.state = state
        self.infoLabels = []
        self.stateLabels = []

        self.createStateLabels()
        self.createInfoLabels()
        self.coin = coin.Coin()


    def createStateLabels(self):
        if self.state == consts.str_main_menu:
            self.stateLabels.append((self.createLabel('1 PLAYER GAME'), (272, 360)))
            self.stateLabels.append((self.createLabel('2 PLAYER GAME'), (272, 405)))
            self.stateLabels.append((self.createLabel('TOP - '), (290, 465)))
            self.stateLabels.append((self.createLabel('000000'), (400, 465)))
        elif self.state == consts.str_load_screen:
            self.stateLabels.append((self.createLabel('WORLD'), (280, 200)))
            self.stateLabels.append((self.createLabel('1 - 1'), (460, 200)))
            self.stateLabels.append((self.createLabel('X   3'), (380, 280)))
            self.playerImage = tools.getImage(setup.photos[consts.str_mario_bros], 178, 32, 12, 16, consts.color_black, consts.bg_scale)

    def createInfoLabels(self):
        self.infoLabels.append((self.createLabel('MARIO'), (75, 30)))
        self.infoLabels.append((self.createLabel('WORLD'), (450, 30)))
        self.infoLabels.append((self.createLabel('TIME'), (625, 30)))
        self.infoLabels.append((self.createLabel('000000'), (75, 55)))
        self.infoLabels.append((self.createLabel('x00'), (300, 55)))
        self.infoLabels.append((self.createLabel('1 - 1'), (480, 55)))

    def createLabel(self, label, fontSize=40, wScale=1.25, hScale=1):
        font = pygame.font.SysFont(consts.font_name, fontSize)
        labelImg = font.render(label, 1, consts.color_white)
        rect = labelImg.get_rect()
        labelImg = pygame.transform.scale(labelImg, (int(rect.width * wScale), int(rect.height * hScale)))
        return labelImg

    def update(self, surface: pygame.Surface):
        self.coin.update()


    def draw(self, surface: pygame.Surface):
        for label in self.stateLabels:
            surface.blit(label[0], label[1])

        for label in self.infoLabels:
            surface.blit(label[0], label[1])

        surface.blit(self.coin.image, self.coin.rect)

        if self.state == consts.str_load_screen:
            surface.blit(self.playerImage, (300, 270))
