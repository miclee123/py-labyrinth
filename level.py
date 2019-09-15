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
                        [2, 21, 8, self.game.wall.concrete],
                        [9, 20, 1, self.game.wall.concrete],
                        [self.game.width - 6, 20, 4, self.game.wall.concrete],
                        [self.game.width - 6, 21, 4, self.game.wall.concrete],
                        [6, 13, 1, self.game.wall.concrete],
                        [6, 14, 3, self.game.wall.concrete],
                        [8, 13, 1, self.game.wall.concrete],
                        [17, 12, 5, self.game.wall.concrete],
                        [20, 20, 2, self.game.wall.concrete],

                        [2, 0, 13, self.game.wall.brick],
                        [16, 0, 12, self.game.wall.brick],
                        [29, 0, 1, self.game.wall.brick],
                        [6, 2, 7, self.game.wall.brick],
                    ],
                    'vertical': [
                        [0, 0, 22, self.game.wall.concrete],
                        [1, 0, 22, self.game.wall.concrete],
                        [self.game.width - 2, 0, 22, self.game.wall.concrete],
                        [self.game.width - 1, 0, 22, self.game.wall.concrete],
                        [17, 10, 2, self.game.wall.concrete],
                        [21, 11, 1, self.game.wall.concrete],
                        [20, 17, 2, self.game.wall.concrete],

                        [24, 1, 2, self.game.wall.brick],
                    ]
                },
                'ladders': [
                    # [15, 15, 6],
                    # [16, 12, 5],
                ],
                'fires': [
                    [7, 13, 1],
                    [18, 11, 3],
                    [10, 20, 10],
                    [22, 20, 4],
                    [10, 21, 16]
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