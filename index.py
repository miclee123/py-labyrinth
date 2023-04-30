#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import *

config = {
    'width': 32,
    'height': 24,
    'bg': '#000',
    'size_x': 60,
    'size_y': 40
}

game = Game(config)
game.start()
