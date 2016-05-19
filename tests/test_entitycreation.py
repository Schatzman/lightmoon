#!/usr/bin/env python

import unittest
from lightmoon.lib.entity_creation import return_stats
from lightmoon.tests.test_resources.test_values import TEST_VALUES

# TODO: 
#   write tests for entity_creation

#   moar char creatio
class TestEntityCreation(unittest.TestCase):

    def setUp(self):
        self.stats_list = TEST_VALUES['return_stats_stats_list']
        self.roll_tuple = TEST_VALUES['resturn_stats_roll_tuple']

    def tearDown(self):
        pass

    def test_return_stats(self):
        self.stats = return_stats(self.stats_list, self.roll_tuple)
        max_stat = self.roll_tuple[0] * self.roll_tuple[1]
        for stat in self.stats:
            self.assertTrue(self.stats[stat] > 0)
            self.assertTrue(self.stats[stat] < max_stat + 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
