#!/usr/bin/env python

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
