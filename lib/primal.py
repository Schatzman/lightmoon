#!/usr/bin/env python

class Entity(object):
    def __init__(self, *args, **kwargs):
        self.alive = True
        self.stats = {}
        if kwargs.get('name'):
            self.name = kwargs.get('name')
        if kwargs.get('stats'):
            self.stats = kwargs.get('stats')