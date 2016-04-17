#!/usr/bin/env python
# DSM 4/16/2016
#
# Run this test file from one folder above lightmoon/.
# Use the following command:
# python3 -m lightmoon.tests.test_primal

import unittest

from lightmoon.lib.primal import Entity

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.entity = Entity()

    def tearDown(self):
        pass

    def test_Entity_alive(self):
        self.assertTrue(self.entity.alive)

    def test_Entity_stats(self):
        self.assertEqual(self.entity.stats, {})

if __name__ == '__main__':
    unittest.main(verbosity=2)