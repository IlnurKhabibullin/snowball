import pygame
from pygame.rect import Rect


class Wall:

    def __init__(self, x, y, w, h, rect=False):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.image.load('images/wall.png')
        self.rect = rect if rect else Rect(x, y, w, h)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.rect == other.rect
