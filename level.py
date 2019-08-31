#!/usr/bin/python
# -*- coding: utf-8 -*-

class Level():
    def __init__(self, game):
        """

        :type game: Game
        """
        self.game = game
        self.levels = [
            {},
            {
                'walls': {
                    'horizontal': [
                        [10, 10, 20, self.game.wall.brick],
                        [2, 21, self.game.width - 4, self.game.wall.concrete]
                    ],
                    'vertical': [
                        [0, 0, 22, self.game.wall.concrete],
                        [1, 0, 22, self.game.wall.concrete],
                        [self.game.width - 2, 0, 22, self.game.wall.concrete],
                        [self.game.width - 1, 0, 22, self.game.wall.concrete],
                    ]
                },
                'ladders': [
                    [15, 15, 6],
                    [16, 12, 5],
                ],
                'fires': [
                    [18, 18, 10]
                ],
                'human': [2, 1]
            }
        ]

    def render(self, level):
        if len(self.levels) > level:
            level_data = self.levels[level]
            walls = level_data.get('walls', {})
            for wall_horizontal in walls.get('horizontal', []):
                self.game.wall.horizontal(*wall_horizontal)
            for wall_vertical in walls.get('vertical', []):
                self.game.wall.vertical(*wall_vertical)
            ladders = level_data.get('ladders', [])
            for ladder in ladders:
                self.game.ladder.ladder(*ladder)
            fires = level_data.get('fires', [])
            for fire in fires:
                self.game.fire.fire(*fire)
            self.game.human.create(*level_data['human'])