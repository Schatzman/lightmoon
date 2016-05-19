#!/usr/bin/env python
# DSM 4/21/2016
"""
lightmoon.tests.test_entitycreation

This script will run tests for lightmoon.lib.entitycreation.
@usage - From the directory above lightmoon, use:
    python -m lightmoon.tests.test_entitycreation
"""
import unittest
from lightmoon.lib.entity_creation import return_stats
from lightmoon.tests.test_resources.test_values import TEST_VALUES

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
