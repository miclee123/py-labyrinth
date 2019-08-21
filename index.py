#!/usr/bin/python
# -*- coding: utf-8 -*-

from game import *

config = {
    'width': 80,
    'height': 60,
    'bg': '#000',
    'step': 20
}

game = Game(config)
game.start()