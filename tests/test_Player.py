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
        self.player = Player()

    def tearDown(self):
        pass

    def test_Player_alive(self):
        self.assertTrue(self.player.alive)

if __name__ == '__main__':
    unittest.main(verbosity=2)