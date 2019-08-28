#!/usr/bin/python
# -*- coding: utf-8 -*-

class Fire():
    def __init__(self, game):
        self.game = game

    def clear(self, x, y):
        self.game.create_rectangle(x, y, x + 1, y + 1, fill=self.game.config['bg'])

    def fire_item(self, x, y, variant=1):
        self.game.coordinates[x][y] = self.game.fire_item
        self.clear(x, y)
        if variant == 1:
            self.game.create_polygon([x, y, x + .5, y + .5, x + 1, y, x + 1, y + 1, x, y + 1], fill='red')
        else:
            self.game.create_polygon([x, y + .5, x + .5, y, x + 1, y + .5, x + 1, y + 1, x, y + 1], fill='red')
        variant += 1
        self.game.tk.after(300, lambda: self.fire_item(x, y, variant % 2))

    def fire(self, x, y, length):
        for i in range(length):
            self.fire_item(x, y)
            x +=1