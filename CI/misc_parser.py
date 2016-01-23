#!/usr/bin/env python

import ConfigParser, os

def parse_misc():
    
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('config.ini')
    
    try: #check if the env already exists, it's better not to mess with existing stuff
        os.environ["verbose"]
        os.environ["always_run"]
    except KeyError:
        os.environ["verbose"] = str(config.getboolean('Misc', 'verbose'))
        os.environ["always_run"] = str(config.getboolean('Misc', 'always_run'))
    else:
        print "\"verbose\" or \"always_run\" already exist as an env variable. Change it to something else."
        exit(1)
