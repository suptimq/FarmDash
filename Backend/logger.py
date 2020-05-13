#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


def set_logging(log_file, log_level=logging.DEBUG):
    """
    Logging to console and log file simultaneously.
    """
    log_format = '[%(asctime)s] - [%(name)s] - [%(levelname)s] - %(message)s'
    formatter = logging.Formatter(log_format)
    logging.basicConfig(level=log_level, format=log_format, filename=log_file)
    # Console Log Handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(log_level)
    logging.getLogger().addHandler(console)
    return logging.getLogger()


# Usage:
#
# logger = set_logging('logfile.log')
# logger.info('Log will save to logfile.log simultaneously.')
# logger.info('This is INFO log.')
# logger.debug('This is DEBUG log.')
