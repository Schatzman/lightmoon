#!/usr/bin/env python
# DSM 4/16/2016
#
# Run this test file from one folder above lightmoon/.
# Use the following command:
# python3 -m lightmoon.tests.test_player

import unittest

from lightmoon.lib.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.name = 'Frank'
        self.ex_stats = {'somestat':1}
        self.player = Player(name=self.name, stats=self.ex_stats)

    def tearDown(self):
        pass

    def test_player_alive(self):
        self.assertTrue(self.player.alive)

    def test_player_stats(self):
        self.assertEqual(self.player.stats, self.ex_stats)

    def test_player_name(self):
        self.assertEqual(self.player.name, self.name)

if __name__ == '__main__':
    unittest.main(verbosity=2)
