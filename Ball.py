import pygame
import math


class Ball:
    """x, y - coordinates, d - a - flight angle, color - RGB tuple"""

    def __init__(self, x, y, a, speed, color):
        self.image = pygame.image.load('images/snowball.png')
        self.rotation_angle = 0
        self.collided = False
        self.countdown = 50
        self.color = color
        self.x = x
        self.y = y
        self.dx = speed * math.sin(a * math.pi / 180)
        self.dy = speed * math.cos(a * math.pi / 180)
