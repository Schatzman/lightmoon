#!/usr/bin/env python

import random

def configure_logging(
                        filename='main.log',
                        format_=(
                            '%(asctime)s user %(name)s @' +
                            ' %(filename)s %(levelname)s: ' +
                            '%(message)s'
                            ),
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=10
                        ):
    import logging
    logging.basicConfig(
            filename=filename,
            format=format_,
            datefmt=datefmt,
            level=level
        )
    return logging

def roll_dice(number_of_dice=3, sides_per_die=6):
    return random.randint(number_of_dice, int(sides_per_die * number_of_dice))
