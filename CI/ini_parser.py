#!/usr/bin/env python

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')

verbose = config.getboolean('Misc', 'verbose')
always_run = config.getboolean('Misc', 'always_run')

token = config.getboolean('Github', 'token')
conditional_prerelease = config.getboolean('Github', 'conditional_prerelease')
conditional_draft = config.getboolean('Github', 'conditional_draft')
prerelease = config.getboolean('Github', 'prerelease')
draft = config.getboolean('Github', 'draft')
description = config.get('Github', 'description')
branch = config.get('Github', 'branch')
packagename = config.get('Github', 'packagename')