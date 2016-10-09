import pygame

from pygame.rect import Rect


class Rowdy:

    def __init__(self, x, y, r, a, name):
        self.name = name
        self.image = pygame.image.load('images/rowdy.png')
        self.x = x
        self.y = y
        self.r = r
        self.a = a
        self.a_t = 0  # time of a last attack
        self.speed = 1
        self.a_s = 1  # attack speed
        self.s_s = 3  # snowball speed
        self.r_a = 0  # rotation angle
        self.rect = Rect(x, y, 50, 50)

    def get_position(self):
        return int(self.x), int(self.y)

    def __str__(self):
        return self.name


class Player(Rowdy):

    def __init__(self, x, y, r, a):
        Rowdy.__init__(self, x, y, r, a)