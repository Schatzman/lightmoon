#!/usr/bin/env python

import random
from lightmoon.conf.settings import DEFAULT_DATE_FORMAT
from lightmoon.conf.settings import DEFAULT_LOGGING_FORMAT
from lightmoon.conf.settings import DEFAULT_LOGGING_LEVEL
from lightmoon.conf.settings import DEFAULT_MAIN_LOGFILE

def configure_logging(
                        filename=DEFAULT_MAIN_LOGFILE,
                        format_=DEFAULT_LOGGING_FORMAT,
                        datefmt=DEFAULT_DATE_FORMAT,
                        level=DEFAULT_LOGGING_LEVEL
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
