#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import logging.config


def obj(key="example01"):
    logging.config.fileConfig("logger.conf")
    logger = logging.getLogger(key)
    return logger
