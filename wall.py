#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageTk


class Wall():

    def __init__(self, game):
        self.game = game
        self.img = Image.open('images/textures/concrete.jpg')
        s = self.game.config['step']
        self.img = self.img.resize((s, s), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.img)

    def brick(self, x, y):
        self.game.create_rectangle(x, y, x + 1, y + 1, fill='red')
        self.game.create_line(x, y, x + 1, y, fill='white')
        self.game.create_line(x, y + .5, x + 1, y + .5, fill='white')
        self.game.create_line(x + .5, y, x + .5, y + .5, fill='white')
        self.game.create_line(x, y + .5, x, y + 1, fill='white')
        self.game.create_line(x + 1, y + .5, x + 1, y + 1, fill='white')
        self.game.coordinates[x][y] = self.game.brick

    def concrete(self, x, y):
        self.game.create_image(x, y, anchor='nw', image=self.image)
        self.game.coordinates[x][y] = self.game.concrete

    def horizontal(self, x, y, length, func):
        for i in range(length):
            func(x, y)
            x += 1

    def vertical(self, x, y, length, func):
        for i in range(length):
            func(x, y)
            y += 1
