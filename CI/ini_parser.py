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

#Github Section    

gh_token = config.getboolean('Github', 'token')
conditional_prerelease = config.getboolean('Github', 'conditional_prerelease')
conditional_draft = config.getboolean('Github', 'conditional_draft')
prerelease = config.getboolean('Github', 'prerelease')
draft = config.getboolean('Github', 'draft')
description = config.get('Github', 'description')
branch = config.get('Github', 'branch')
packagename = config.get('Github', 'packagename')

try:
    os.environ["gh_token"]
except KeyError:
    if gh_token:
        os.environ["gh_token"] = "true"
        wait_to_deploy = True #there is a token and we want to deploy
    else: #this includes None
        os.environ["gh_token"] = "false"
else:
    print "\"gh_token\" already exists as an env variable. change it to something else."
    exit(1)

try:
    os.environ["conditional_prerelease"]
except KeyError:
    if conditional_prerelease:
        os.environ["conditional_prerelease"] = "true"
    else:
        os.environ["conditional_prerelease"] = "false"
else:
    print "\"conditional_prerelease\" already exists as an env variable. change it to something else."
    exit(1)
    
try:
    os.environ["conditional_draft"]
except KeyError:
    if conditional_draft:
        os.environ["conditional_draft"] = "true"
    else:
        os.environ["conditional_draft"] = "false"
else:
    print "\"conditional_draft\" already exists as an env variable. change it to something else."
    exit(1)
    
try:
    os.environ["prerelease"]
except prerelease:
    if always_run:
        os.environ["prerelease"] = "true"
    else:
        os.environ["prerelease"] = "false"
else:
    print "\"prerelease\" already exists as an env variable. change it to something else."
    exit(1)
    
try:
    os.environ["draft"]
except KeyError:
    if draft:
        os.environ["draft"] = "true"
    else:
        os.environ["draft"] = "false"
else:
    print "\"draft\" already exists as an env variable. change it to something else."
    exit(1)
