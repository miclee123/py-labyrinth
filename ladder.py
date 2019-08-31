#!/usr/bin/python
# -*- coding: utf-8 -*-

class Ladder():

    def __init__(self, game):
        self.game = game
        self.color = 'blue'

    def rang(self, x, y):
        s = self.game.config['step']
        w = 4
        self.game.create_line(x + .2, y, x + .2, y + 1, fill=self.color, width=w)
        self.game.create_line(x + .8, y, x + .8, y + 1, fill=self.color, width=w)
        self.game.create_line(x + .1, y + .2, x + .9, y + .2, fill=self.color, width=w)
        self.game.create_line(x + .1, y + .7, x + .9, y + .7, fill=self.color, width=w)
        self.game.coordinates[x][y] = self.game.rang

    def ladder(self, x, y, length):
        for i in range(length):
            self.rang(x, y)
            y +=1