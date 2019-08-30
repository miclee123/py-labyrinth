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
                        [10, 10, 20, self.game.wall.brick]
                    ],
                    'vertical': [
                        [30, 30, 10, self.game.wall.concrete]
                    ]
                },
                'ladders': [
                    [25, 20, 5],
                    [26, 20, 25],
                ],
                'fires': [
                    [35, 35, 10]
                ],
                'human': [20, 20]
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