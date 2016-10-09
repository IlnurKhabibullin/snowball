import pygame


class Rowdy:

    def __init__(self, x, y, r, a):
        self.image = pygame.image.load('images/rowdy.png')
        self.x = x
        self.y = y
        self.r = r
        self.a = a
        self.a_t = 0  # time of a last attack
        self.speed = 1
        self.a_s = 1  # attack speed
        self.s_s = 1  # snowball speed
        self.r_a = 0  # rotation angle

    def get_position(self):
        return int(self.x), int(self.y)


class Player(Rowdy):

    def __init__(self, x, y, r, a):
        Rowdy.__init__(self, x, y, r, a)