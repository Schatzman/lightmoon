#!/usr/bin/env python
# DSM 4/16/2016
"""
lightmoon.lib.player

Contains the Player class which inherits from the Entity class.
"""
from lightmoon.lib.primal import Entity

class Player(Entity):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
