#!/usr/bin/env python

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')

verbose = config.getboolean('Misc', 'verbose')
always_run = config.getboolean('Misc', 'always_run')

