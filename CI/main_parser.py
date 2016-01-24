#!/usr/bin/env python

from misc_parser import parse_misc
from gh_parser import parse_gh
from asset_parser import parse_asset
from docs_parser import parse_docs
from deploy_setup import deploy_setup

import copy, os

parse_misc()

try: #check if the env already exists, it's better not to mess with existing stuff
    os.environ["wait_to_deploy"]
except KeyError:
    if os.environ["always_run"] == "True":
        os.environ["wait_to_deploy"] = "False"
    else:
        os.environ["wait_to_deploy"] = "True"
else:
    print "\"wait_to_deploy\" already exists as an env variable. change it to something else."
    exit(1)

rebuild_yml = {
    "language": ["objective-c"],
    "install": ["sh ./CI/unity_install.sh"],
    "script": ["sh ./CI/unity_build.sh"],
    "before_deploy": ["sh ./CI/pre_deploy.sh"],
    "deploy": [],
    "env": {
        "global": [
            "verbose=%s" % os.environ["verbose"],
            "packagename=%s" % os.environ["packagename"],
            "include_version=%s" % os.environ["include_version"]
        ]
    }
}

if os.environ["TRAVIS_PULL_REQUEST"] == "false" and os.environ["TRAVIS_TAG"].strip():
    
    deploy_yml = copy.deepcopy(rebuild_yml) #yes it's slow, but there's no real substitute from what I could gather
    
    ini_docs = parse_docs()
    if ini_docs:
        deploy_yml["deploy"].append(ini_docs)
        print '------------------------------------------------------------------------------------------------------------------------'
        print "Deployment to Github Pages accepted. -----------------------------------------------------------------------------------"
        print '------------------------------------------------------------------------------------------------------------------------'
    
    ini_gh = parse_gh()
    if ini_gh:
        deploy_yml["deploy"].append(ini_gh)
        print '------------------------------------------------------------------------------------------------------------------------'
        print "Deployment to Github Releases accepted. --------------------------------------------------------------------------------"
        print '------------------------------------------------------------------------------------------------------------------------'
    
    ini_asset = parse_asset()
    if ini_asset:
        deploy_yml["deploy"].append(ini_asset)
        print '------------------------------------------------------------------------------------------------------------------------'
        print "Deployment to Unity's Asset Store accepted. ----------------------------------------------------------------------------"
        print '------------------------------------------------------------------------------------------------------------------------'
    
    if rebuild_yml == deploy_yml:
        print '------------------------------------------------------------------------------------------------------------------------'
        print "Skipping deployment. ---------------------------------------------------------------------------------------------------"
        print '------------------------------------------------------------------------------------------------------------------------'
    else:
        os.environ["wait_to_deploy"] = "True"
        deploy_setup(os.environ["GH_TOKEN"], deploy_yml)
    
else:
    print '------------------------------------------------------------------------------------------------------------------------'
    print "Skipping deployment. ---------------------------------------------------------------------------------------------------"
    print '------------------------------------------------------------------------------------------------------------------------'

#you only get here if there is no deployment since deploy_setup calls exit on success.
os.system("sh ./CI/unity_install.sh") #move on to the build steps. This needs to be invoked like this to be able to pass the env vars created here.
os.system("sh ./CI/unity_build.sh")
