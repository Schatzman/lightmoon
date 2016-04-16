#!/usr/bin/env python

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
