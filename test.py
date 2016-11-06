import os
import pygame
import snowball_object
from pygame.rect import Rect
from pygame import time
from pygame.time import Clock

w = 1024
h = 576


def load_images():
    return {name: pygame.image.load(os.path.join(root, name))
            for root, dirs, files in os.walk('images')
            for name in files
            if name.endswith(".png")}


images = load_images()
pygame.init()
pygame.display.init()
clock = Clock()
screen = pygame.display.set_mode((w, h))
eternity = True
frame = 0

collidable1 = snowball_object.Collidable(50, 50, 100, 100, 0, Rect(50, 50, 100, 100))
movable1 = snowball_object.Movable(350, 350, 150, 150, 0, Rect(350, 350, 150, 150))
objects = [collidable1, movable1]

while eternity:
    # FRAMES per second. Lesser value, slower game goes
    pressedList = pygame.key.get_pressed()
    if pressedList[pygame.K_ESCAPE]:
        eternity = False
    screen.fill((255, 255, 255))
    pygame.event.pump()
    for snow_object in objects:
        snow_object.update_animation(frame)
        # if cur_time - snow_object.a_cur_time > snow_object.a_time:
        #     snow_object.a_cur_time = cur_time
        #     # need to ckeck for default_status while releasing the button
        #     if snow_object.a_step == len(snow_object.a_dict[snow_object.a_status]) - 1:
        #         snow_object.a_status = snow_object.default_status
        #         snow_object.a_step = 0
        #     else:
        #         snow_object.a_step += 1
        snow_image = images[snow_object.get_image()]
        snow_image = pygame.transform.rotate(snow_image, snow_object.a)
        snow_image = pygame.transform.scale(snow_image,
                                            (snow_object.w, snow_object.h))
        screen.blit(snow_image,
                    (int(snow_object.x), int(snow_object.y)))
            # if pressedList[pygame.K_KP4]:
            #     rowdy.a -= 1
            #     xd1 = rowdy.r * math.cos(rowdy.a * math.pi / 180)
            #     yd1 = rowdy.r * math.sin(rowdy.a * math.pi / 180)
            # if pressedList[pygame.K_KP6]:
            #     rowdy.a += 1
            #     xd1 = rowdy.r * math.cos(rowdy.a * math.pi / 180)
            #     yd1 = rowdy.r * math.sin(rowdy.a * math.pi / 180)
            # if pressedList[pygame.K_KP5]:
            #     shoot(rowdy)
            # if rowdy.a == 180:
            #     rowdy.a = -180
            # for b in snowballs:
            #     move_bullets(b)
            # x, y = rowdy.get_position()
            # for person in shooting_rowdies:
            #     cooldown_action(person)

            # screen.blit(pygame.transform.rotate(rowdy.image, rowdy.a), (int(rowdy.x), int(rowdy.y)))
            # screen.blit(images['rowdy.png'], (50, 50))
            # for wall in walls:
            #     screen.blit(wall.image, (int(wall.x), int(wall.y)))
            #     pygame.draw.rect(screen, (255, 0, 0), wall.rect, 2)
            # for b in snowballs:
            #     b.rotation_angle += 1.0
            #     b.rotation_angle %= 360
            #     screen.blit(pygame.transform.rotate(b.image, b.rotation_angle),
            #                 (int(b.x), int(b.y)))
            #     pygame.draw.rect(screen, (255, 0, 0), b.rect, 2)
            # l = b.rect.collidedictall(collidables, 1)
            # if l:
            #     for c in l:
            #         collidables.pop(c[0])
            #         walls.remove(c[0])
            #     b.collided = True
            # if not walls:
            #     eternity = False
    pygame.display.flip()
    clock.tick(30)
    frame += 1
pygame.display.quit()
pygame.quit()
