#!/usr/bin/python
# -*- coding: utf-8 -*-

class Wall():
    def __init__(self, game):
        self.game = game

    def brick(self, x, y):
        """

        :type game: Game
        """
        s = self.game.config['step']
        c = self.game.canvas
        c.create_rectangle(x * s, y * s, (x + 1) * s, (y + 1) * s, fill='red', outline='')
        c.create_line(x * s, y * s, (x + 1) * s, y * s, fill='white')
        c.create_line(x * s, (y + .5) * s, (x + 1) * s, (y + .5) * s, fill='white')
        c.create_line((x + .5) * s, y * s, (x + .5) * s, (y + .5) * s, fill='white')
        c.create_line(x * s, (y + .5) * s, x * s, (y + 1) * s, fill='white')
        c.create_line((x + 1) * s, (y + .5) * s, (x + 1) * s, (y + 1) * s, fill='white')

    def horizontal(self, x, y, length):
        for i in range(length):
            self.brick(x, y)
            x += 1

    def vertical(self, x, y, length):
        for i in range(length):
            self.brick(x, y)
            y += 1
