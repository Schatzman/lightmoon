#!/usr/bin/env python

from lightmoon.lib.primal import Entity

class Player(Entity):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
