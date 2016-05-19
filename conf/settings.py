#!/usr/bin/env python
# DSM 5/19/2016
"""
lightmoon.conf.settings

This file contains constants which can be imported and used
throughout the project.
@Usage:
    from lightmoon.conf.settings import SOME_CONSTANT
"""
#####################################################################
# LOGGING SETTINGS                                                  #
#####################################################################
DEFAULT_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
DEFAULT_LOGGING_FORMAT = (
        '%(asctime)s user %(name)s @' +
        ' %(filename)s %(levelname)s: ' +
        '%(message)s'
    ),
DEFAULT_LOGGING_LEVEL = 10
DEFAULT_MAIN_LOGFILE = 'main.log'
