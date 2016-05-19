#!/usr/bin/env python

from lightmoon.lib.util import roll_dice

def return_stats(stats_list, roll_tuple):
    number_of_dice = roll_tuple[0]
    sides_per_die = roll_tuple[1]
    return { # dictionary comprehension
        stat: roll_dice(number_of_dice, sides_per_die) for stat in stats_list
    }