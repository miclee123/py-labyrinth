#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

from wall import Wall


class Game():
    def __init__(self, config):
        self.empty = 'empty'
        self.config = config
        self.size = self.config['step']
        self.tk = Tk()
        self.coordinates = [[self.empty + str(i)] * config['height'] for i in range(config['width'])]

        self.canvas = Canvas()
        self.canvas.create_rectangle(0, 0, self.config['width'] * self.size, self.config['height'] * self.size,
                                     fill=config['bg'])
        self.canvas.pack(fill=BOTH, expand=1)

    def start(self):
        self.tk.bind('<Left>', self.pr)
        wall = Wall(self)
        wall.horizontal(10, 10, 20)
        wall.vertical(30, 30, 10)
        self.tk.geometry(str(self.config['width'] * self.size) + 'x' + str(self.config['height'] * self.size))
        self.tk.mainloop()

    def pr(self, event):
        print('left')
