#!/usr/bin/env python
# DSM 4/21/2016
"""
lightmoon.tests.test_entity

This script will run tests for lightmoon.lib.primal.Entity.
@usage - From the directory above lightmoon, use:
    python -m lightmoon.tests.test_entity
"""
import unittest

from lightmoon.lib.primal import Entity

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.entity = Entity()

    def tearDown(self):
        pass

    def test_entity_alive(self):
        self.assertTrue(self.entity.alive)

    def test_entity_stats(self):
        self.assertEqual(self.entity.stats, {})

if __name__ == '__main__':
    unittest.main(verbosity=2)
