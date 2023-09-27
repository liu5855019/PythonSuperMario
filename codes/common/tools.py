import os
import pygame
import random
import consts


def loadPhotos(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    photos = {}
    files = os.listdir(path)
    for file in files:
        name, ext = os.path.splitext(file)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, file))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            photos[name] = img
    return photos


def getImage(photo: pygame.Surface, x, y, w, h, colorKey, scale):
    img = pygame.Surface((w, h))
    img.blit(photo, (0, 0), (x, y, w, h))
    img.set_colorkey(colorKey)

    img = pygame.transform.scale(img, (int(w * scale), int(h * scale)))
    return img


def reSize(width: float, height: float, scale: float):
    return int(width * scale), int(height * scale)


def randomColor():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def createLabel(string, fontSize = consts.font_size, wScale=1.25, hScale=1, color = consts.color_white):
    font = pygame.font.SysFont(consts.font_name, fontSize)
    label = font.render(str(string), 1, color)
    rect = label.get_rect()
    label = pygame.transform.scale(label, (int(rect.width * wScale), int(rect.height * hScale)))
    return label
