#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

    def run(self, window, name, menu_option):
        pass
