import os
import pygame
import time
import random
import math

from pygame.rect import Rect

import rowdy
import ball
from wall import Wall

images = {}


def load_images():
    input_files = os.listdir('images')
    for input_file in input_files:
        image = pygame.image.load('images/' + input_file)
        images[input_file] = image

load_images()
rowdy = rowdy.Rowdy(512, 76, 30, 0, 'Buddy')
shooting_rowdies = []
snowballs = []
wall1 = Wall(507, 200, 20, 20)
walls = [wall1]
collidables = {wall1: wall1.rect}
green = (0, 255, 0)
red = (255, 0, 0)
t = 0
w = 1024
h = 576
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((w, h))
eternity = True
xd1 = 0
yd1 = 30


def move(someone, keys):
    ds = map(lambda dx, dy, z: someone.speed * (dx - dy) + z, keys[1], keys[0], [someone.y, someone.x])
    if int(ds[1]) in range(0, w - 50) and int(ds[0]) in range(0, h - 40):
        someone.y, someone.x = ds[0], ds[1]


def shoot(someone):
    if time.time() - someone.a_t > someone.a_s:
        someone.a_t = time.time()
        shooting_rowdies.append(someone)
        dx = someone.x + 20
        dy = someone.y + 20
        dx -= 20 * math.cos(someone.a * math.pi / 180)
        dy += 20 * math.sin(someone.a * math.pi / 180)
        snowballs.append(ball.Ball(dx, dy, someone.a, someone.s_s, green, rowdy))


def cooldown_action(someone):
    someone.image = pygame.image.load('images/rowdy_shoot.png')
    if time.time() - someone.a_t > someone.a_s:
        someone.image = pygame.image.load('images/rowdy.png')


def generate_walls():
    walls_count = random.randint(3, 10)
    print '{} walls generated'.format(walls_count)
    for i in range(walls_count):
        wx = random.randint(0, w - 20)
        wy = random.randint(0, h - 20)
        new_rect = Rect(wx, wy, 20, 20)
        if not new_rect.collidedict(collidables):
            new_wall = Wall(wx, wy, 20, 20, new_rect)
            walls.append(new_wall)
            collidables[new_wall] = new_wall.rect



def move_bullets(someone):
    if someone.collided is True:
        collide_action(someone)
    elif not (int(someone.x) in range(0, w) and int(someone.y) in range(0, h)):
        someone.collided = True
        collide_action(someone)
    else:
        someone.x += someone.dx
        someone.y += someone.dy
        someone.rect.x = someone.x
        someone.rect.y = someone.y


def collide_action(ball):
    pygame.draw.circle(screen, ball.color, (int(ball.x), int(ball.y)), (6 - ball.countdown / 10) * 3, 0)
    ball.countdown -= 1
    if ball.countdown > 40:
        ball.color = (114, 241, 213)
    elif ball.countdown > 30:
        ball.color = (114, 241, 213)
    elif ball.countdown > 20:
        ball.color = (114, 207, 241)
    elif ball.countdown > 10:
        ball.color = (30, 163, 212)
    elif ball.countdown > 0:
        ball.color = (30, 163, 212)
    else:
        snowballs.remove(ball)


generate_walls()
while eternity:
    pressedList = pygame.key.get_pressed()
    if pressedList[pygame.K_ESCAPE]:
        eternity = False
    screen.fill((255, 255, 255))
    pygame.event.pump()
    move(rowdy, [[pressedList[pygame.K_UP], pressedList[pygame.K_LEFT]],
         [pressedList[pygame.K_DOWN], pressedList[pygame.K_RIGHT]]])
    if pressedList[pygame.K_KP4]:
        rowdy.a -= 1
        xd1 = rowdy.r * math.cos(rowdy.a * math.pi / 180)
        yd1 = rowdy.r * math.sin(rowdy.a * math.pi / 180)
    if pressedList[pygame.K_KP6]:
        rowdy.a += 1
        xd1 = rowdy.r * math.cos(rowdy.a * math.pi / 180)
        yd1 = rowdy.r * math.sin(rowdy.a * math.pi / 180)
    if pressedList[pygame.K_KP5]:
        shoot(rowdy)
    if rowdy.a == 180:
        rowdy.a = -180
    for b in snowballs:
        move_bullets(b)
    x, y = rowdy.get_position()
    for person in shooting_rowdies:
        cooldown_action(person)

    screen.blit(pygame.transform.rotate(rowdy.image, rowdy.a), (int(rowdy.x), int(rowdy.y)))
    screen.blit(images['rowdy.png'], (50, 50))
    for wall in walls:
        screen.blit(wall.image, (int(wall.x), int(wall.y)))
        # pygame.draw.rect(screen, (255, 0, 0), wall.rect, 2)
    for b in snowballs:
        b.rotation_angle += 1.0
        b.rotation_angle %= 360
        screen.blit(pygame.transform.rotate(b.image, b.rotation_angle),
                    (int(b.x), int(b.y)))
        # pygame.draw.rect(screen, (255, 0, 0), b.rect, 2)
        l = b.rect.collidedictall(collidables, 1)
        if l:
            for c in l:
                collidables.pop(c[0])
                walls.remove(c[0])
            b.collided = True
        if not walls:
            eternity = False
    pygame.display.flip()
pygame.display.quit()
pygame.quit()
