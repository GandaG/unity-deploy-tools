#!/usr/bin/env python

import ConfigParser

wait_to_deploy = False #check to see if there is going to be a rebuild (if there are any deployment tokens present.)

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read('config.ini')

#Misc Section

verbose = config.getboolean('Misc', 'verbose')
always_run = config.getboolean('Misc', 'always_run')

try:
    os.environ["verbose"]
except KeyError:
    if verbose:
        os.environ["verbose"] = "true"
    else:
        os.environ["verbose"] = "false"
else:
    print "\"verbose\" already exists as an env variable. change it to something else."
    exit(1)

try:
    os.environ["always_run"]
except KeyError:
    if always_run:
        os.environ["always_run"] = "true"
    else:
        os.environ["always_run"] = "false"
else:
    print "\"always_run\" already exists as an env variable. change it to something else."
    exit(1)


