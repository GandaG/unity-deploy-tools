#!/usr/bin/env python

import ConfigParser, os, json

def parse_misc():
    
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('.deploy.ini')
    
    try: #check if the env already exists, it's better not to mess with existing stuff
        os.environ["verbose"]
        os.environ["always_run"]
    except KeyError:
        os.environ["verbose"] = str(config.getboolean('Misc', 'verbose'))
        os.environ["always_run"] = str(config.getboolean('Misc', 'always_run'))
    else:
        print "Something in [Misc] already exists as an env variable. Change it to something else."
        exit(1)

def parse_unity_version():
    
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('.deploy.ini')
    
    unity_vers = config.get('Misc', 'unity_version')
    
    if not unity_vers:
        return "5.0.1" #once/if a scraper is written this should return the latest version.
    
    return unity_vers
    
def get_available_unity_vers():
    
    #once/if a scraper is written, this should output the scraper's results instead of a fixed list.
    with open('.deploy/travis/unity_supported_versions.json') as data_file:    
        data = json.load(data_file)
    
    return data


