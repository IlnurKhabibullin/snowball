import os
import re
import uuid

import math
from pygame import time


# idea is that each object will have inner state and outer force.
# f.e. player that pressed button, assigned to move, will be an outer force.
# this outer force will change some vars of object (dx, dy) and object will
# change an inner state.
# Object's vars will vary on inners and outers.
# Outers - vars, that will be changing because of outer forces.
# Inners - vars, that will be changing because of current state of object.
# Object itself should have functions to update it's inners
# and functions to change outers from outer forces
# Animation change/update is outer force.

# As example. Rowdy moves down (angle = 0). Player rotated Rowdy and it's angle
# has changed. So, angle is outer.
# Rowdy's x and y are changing depending on angle. They're inners.


# Need to count frames, not time

class Collidable:
    """
    :param x:
    :param y:
    :param w: width
    :param h: height
    :param a: angle
    :param cb: collider box. Pygame's Rect object.
    """

    @staticmethod
    def natural_key(string_):
        return [int(s) if s.isdigit() else s for s in
                re.split(r'(\d+)', string_)]

    def __init__(self, x, y, w, h, a, cb):
        # 'a_' prefix for animation variables

        # unchangeable vars
        self.uuid = uuid.uuid4()
        self.default_status = 'idle'
        # list of images' names, using for animation cycle
        self.a_dict = {'idle': sorted(os.listdir('images/collidable'),
                                      key=Collidable.natural_key)}

        # outers
        self.a_status = self.default_status
        self.a_list = self.a_dict[self.a_status]
        # frames amount for animation image change
        self.a_frame_rate = 15
        self.w = w
        self.h = h
        self.cb = cb
        self.a = a

        # inners
        self.x = x
        self.y = y
        self.a_step = 0
        self.a_start_frame = 0

    def __eq__(self, other):
        return self.uuid == other.uuid

    def get_image(self):
        return self.a_list[self.a_step]

    def a_idle(self):
        self.a_status = 'idle'
        self.a_step = 0

    def update_animation(self, frame):
        if frame - self.a_start_frame > self.a_frame_rate:
            self.a_start_frame = frame
            # need to ckeck for default_status while releasing the button
            if self.a_step == len(self.a_list) - 1:
                self.a_step = 0
            else:
                self.a_step += 1


class Movable(Collidable):
    """
    functions with 'a_' for assigning current animation (on move button pressed)
    """
    def __init__(self, x, y, w, h, a, cb):
        Collidable.__init__(self, x, y, w, h, a, cb)
        self.speed = 3
        self.dx, self.dy = self.set_direction()
        self.a_dict = {'idle': sorted(os.listdir('images/movable'),
                                      key=Movable.natural_key)}
        self.a_list = self.a_dict[self.a_status]
        self.a_frame_rate = 30

    def set_direction(self):
        return self.speed * math.sin(self.a * math.pi / 180), \
               self.speed * math.cos(self.a * math.pi / 180)

    def a_move(self):
        self.a_status = 'move'
        self.a_step = 0
        # need to use it only when angle is changing
