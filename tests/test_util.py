#!/usr/bin/env python

import random # random testing is bad. so what? I do what I want.
import unittest
from lightmoon.lib.util import roll_dice

class TestUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_roll_dice_1d6(self):
        one_rolled = False
        six_rolled = False
        for i in xrange(10000):
            result = roll_dice(1,6)
            self.assertTrue(result > 0)
            self.assertTrue(result < 7)
            if result == 1:
                one_rolled = True
            if result == 6:
                six_rolled = True
        self.assertTrue(one_rolled) # watch the world burn
        self.assertTrue(six_rolled)

    def test_roll_dice_0dRAN(self): # Ahhhhhh!
        for i in xrange(10000):     # yep, 10000 times.
            result = roll_dice(0, random.randint(1,1000))
            self.assertEqual(result, 0)

    def test_roll_dice_many(self):
        for i in xrange(10000):
            number_of_dice = random.randint(1, 10)
            number_of_sides = random.randint(1, 100)
            maximum_roll = number_of_dice * number_of_sides
            result = roll_dice(number_of_dice, number_of_sides)
            self.assertTrue(result > 0)
            self.assertTrue(result < maximum_roll + 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
