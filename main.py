import pygame
import time
import random
import math
import Rowdy
import Ball

rowdy = Rowdy.Rowdy(512, 76, 30, 0)
shooting_rowdies = []
snowballs = []
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
    ds = map(lambda x, y, z: someone.speed * (x - y) + z, keys[1], keys[0], [someone.y, someone.x])
    if int(ds[1]) in range(6, w - 6) and int(ds[0]) in range(6, h - 6):
        someone.y, someone.x = ds[0], ds[1]


def shoot(someone):
    if time.time() - someone.a_t > someone.a_s:
        someone.a_t = time.time()
        shooting_rowdies.append(someone)
        snowballs.append(Ball.Ball(someone.x, someone.y, someone.a, green))


def cooldown_action(someone):
    someone.image = pygame.image.load('images/rowdy_shoot.png')
    if time.time() - someone.a_t > someone.a_s:
        someone.image = pygame.image.load('images/rowdy.png')


def move_bullets(someone):
    if someone.collided is True:
        collide_action(someone)
    elif not (int(someone.x) in range(0, w) and int(someone.y) in range(0, h)):
        someone.collided = True
        collide_action(someone)
    else:
        someone.x += someone.dx
        someone.y += someone.dy


def collide_action(ball):
    # pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), (6 - self.countdown / 10) * 3, 0)
    ball.countdown -= 1
    if ball.countdown > 40:
        ball.color = (128, 255, 0)
    elif ball.countdown > 30:
        ball.color = (128, 128, 0)
    elif ball.countdown > 20:
        ball.color = (172, 128, 0)
    elif ball.countdown > 10:
        ball.color = (255, 128, 0)
    elif ball.countdown > 0:
        ball.color = (255, 0, 0)
    else:
        snowballs.remove(ball)

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
    # pygame.draw.circle(screen, (255, 0, 0), (x, y), 12, 0)
    # pygame.draw.line(screen, (0, 0, 255), (x, y), (xd1 + x, yd1 + y), 3)
    for b in snowballs:
        b.rotation_angle += 1.0
        b.rotation_angle %= 360
        screen.blit(pygame.transform.rotate(b.image, b.rotation_angle),
                    (int(b.x), int(b.y)))
        # pygame.draw.circle(screen, b.color,(int(b.x), int(b.y)),3,0)
    pygame.display.flip()
pygame.display.quit()
pygame.quit()
