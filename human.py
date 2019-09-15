#!/usr/bin/python
# -*- coding: utf-8 -*-

class Human():

    def __init__(self, game):
        """

        :type game: Game
        """
        self.game = game
        self.width = 4
        self.is_falling = False
        game.tk.bind('<Left>', self.left)
        game.tk.bind('<Right>', self.right)
        game.tk.bind('<Up>', self.up)
        game.tk.bind('<Down>', self.down)

    def create(self, x, y):
        self.x = x
        self.y = y
        self.draw()
        self.fall()

    def draw(self, x = None, y = None, color='#cc87d9'):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.game.create_line(x + .5, y, x + .5, y + .7, fill=color, width=self.width)
        self.game.create_line(x + .5, y + .7, x + .2, y + 1, fill=color, width=self.width)
        self.game.create_line(x + .5, y + .7, x + .8, y + 1, fill=color, width=self.width)
        self.game.create_line(x + .2, y + .4, x + .8, y + .4, fill=color, width=self.width)
        self.game.create_oval(x + .4, y, x + .6, y + .3, fill=color)

    def left(self, event):
        if not self.is_falling \
                and self.x > 0 \
                and self.left_item() in [self.game.empty, self.game.rang]:
            self.clear()
            self.x -= 1
            self.draw()
            self.fall()

    def right(self, event):
        if not self.is_falling \
                and self.x < self.game.config['width'] - 1 \
                and self.right_item() in [self.game.empty, self.game.rang]:
            self.clear()
            self.x += 1
            self.draw()
            self.fall()

    def up(self, event):
        if self.y > 0 \
                and self.current_item() in [self.game.rang] \
                and self.top_item() in [self.game.empty, self.game.rang]:
            self.clear()
            self.y -= 1
            self.draw()

    def down(self, event=None):
        if self.y < self.game.config['height'] - 1 \
                and self.current_item() in [self.game.empty, self.game.rang] \
                and self.bottom_item() in [self.game.empty, self.game.rang]:
            self.clear()
            self.y += 1
            self.draw()
            self.fall()

    def fall(self):
        if self.y < self.game.config['height'] - 1 \
                and self.current_item() in [self.game.empty] \
                and self.bottom_item() in [self.game.empty]:
            self.clear()
            self.is_falling = True
            self.y += 1
            self.draw()
            self.game.tk.after(500, lambda: self.fall())
        else:
            self.is_falling = False

    def clear(self, restore_item=True):
        self.game.create_rectangle(self.x, self.y, self.x + 1, self.y + 1, fill=self.game.config['bg'])
        if restore_item:
            if self.current_item() == self.game.rang:
                self.game.ladder.rang(self.x, self.y)

    def current_item(self):
        return self.game.coordinates[self.x][self.y]

    def left_item(self):
        if self.x > 0:
            return self.game.coordinates[self.x - 1][self.y]
        return None

    def right_item(self):
        if self.x < self.game.config['width'] - 1:
            return self.game.coordinates[self.x + 1][self.y]
        return None

    def top_item(self):
        if self.y > 0:
            return self.game.coordinates[self.x][self.y - 1]

    def bottom_item(self):
        if self.y < self.game.config['height'] - 1:
            return self.game.coordinates[self.x][self.y + 1]
