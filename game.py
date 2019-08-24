#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

from fire import Fire
from ladder import Ladder
from wall import Wall
from human import Human


class Game():
    def __init__(self, config):
        self.empty = 'empty'
        self.brick = 'brick'
        self.rang = 'rang'
        self.concrete = 'concrete'
        self.config = config
        self.size = self.config['step']
        self.tk = Tk()
        self.coordinates = [[self.empty] * config['height'] for i in range(config['width'])]

        self.canvas = Canvas()
        self.canvas.create_rectangle(0, 0, self.config['width'] * self.size, self.config['height'] * self.size,
                                     fill=config['bg'])
        self.canvas.pack(fill=BOTH, expand=1)

    def start(self):
        self.wall = Wall(self)
        self.wall.horizontal(10, 10, 20, self.wall.brick)
        self.wall.vertical(30, 30, 10, self.wall.concrete)
        self.wall.concrete(10, 11)
        self.ladder = Ladder(self)
        self.ladder.ladder(25, 20, 5)
        self.ladder.ladder(26, 20, 5)
        self.human = Human(20, 20, self)
        self.fire = Fire(self)
        self.fire.fire(35, 35, 10)
        self.tk.geometry(str(self.config['width'] * self.size) + 'x' + str(self.config['height'] * self.size))
        self.tk.mainloop()

    def create_line(self, x1, y1, x2, y2, **kwargs):
        s = self.config['step']
        self.canvas.create_line(x1 * s, y1 * s, x2 * s, y2 * s, kwargs)

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        s = self.config['step']
        self.canvas.create_rectangle(x1 * s, y1 * s, x2 * s, y2 * s, kwargs)

    def create_oval(self, x1, y1, x2, y2, **kwargs):
        s = self.config['step']
        self.canvas.create_oval(x1 * s, y1 * s, x2 * s, y2 * s, kwargs)

    def create_polygon(self, points, **kwargs):
        s = self.config['step']
        points_by_size = []
        for i in points:
            points_by_size.append(i * s)
        self.canvas.create_polygon(points_by_size, kwargs)

    def create_image(self, x, y, **kwargs):
        s = self.config['step']
        self.canvas.create_image(x * s, y * s, kwargs)