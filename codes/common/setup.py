import pygame

import consts
import tools

pygame.init()
screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))

photos = tools.loadPhotos(consts.path_graphics)


