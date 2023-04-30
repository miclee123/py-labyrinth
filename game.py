#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

from fire import Fire
from ladder import Ladder
from level import Level
from wall import Wall
from human import Human


class Game():
    def __init__(self, config):
        self.level = None
        self.empty = 'empty'
        self.brick = 'brick'
        self.rang = 'rang'
        self.concrete = 'concrete'
        self.fire_item = 'fire'
        self.config = config
        self.width = config['width']
        self.height = config['height']
        self.size_x = self.config['size_x']
        self.size_y = self.config['size_y']
        self.tk = Tk()
        self.coordinates = [[self.empty] * self.height for i in range(self.width)]

        self.canvas = Canvas()
        self.create_rectangle(0, 0, self.width, self.height,
                              fill=config['bg'])
        self.canvas.pack(fill=BOTH, expand=1)
        self.wall = Wall(self)
        self.ladder = Ladder(self)
        self.fire = Fire(self)
        self.human = Human(self)

    def start(self):
        self.tk.geometry(str(self.config['width'] * self.size_x) + 'x' + str(self.config['height'] * self.size_y))
        self.level = Level(self)
        self.level.render(1)
        self.tk.mainloop()

    def create_line(self, x1, y1, x2, y2, **kwargs):
        self.canvas.create_line(x1 * self.size_x, y1 * self.size_y, x2 * self.size_x, y2 * self.size_y, kwargs)

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        self.canvas.create_rectangle(x1 * self.size_x, y1 * self.size_y, x2 * self.size_x, y2 * self.size_y, kwargs)

    def create_oval(self, x1, y1, x2, y2, **kwargs):
        self.canvas.create_oval(x1 * self.size_x, y1 * self.size_y, x2 * self.size_x, y2 * self.size_y, kwargs)

    def create_polygon(self, points, **kwargs):
        points_by_size = []
        j = 0
        for i in points:
            points_by_size.append(i * (self.size_x if j % 2 == 0 else self.size_y))
            j += 1
        self.canvas.create_polygon(points_by_size, kwargs)

    def create_image(self, x, y, **kwargs):
        self.canvas.create_image(x * self.size_x, y * self.size_y, kwargs)
