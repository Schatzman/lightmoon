#!/usr/bin/env python
# DSM 4/16/2016
#
# Run this test file from one folder above lightmoon/.
# Use the following command:
# python3 -m lightmoon.tests.test_player

import unittest

from lightmoon.lib.nonplayer import NonPlayer

class TestNonPlayer(unittest.TestCase):
    def setUp(self):
        self.nonplayer = NonPlayer()

    def tearDown(self):
        pass

    def test_NonPlayer_alive(self):
        self.assertTrue(self.nonplayer.alive)

    def test_NonPlayer_stats(self):
        self.assertEqual(self.nonplayer.stats, {})

if __name__ == '__main__':
    unittest.main(verbosity=2)