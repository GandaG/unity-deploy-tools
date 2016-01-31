#!/usr/bin/env python

from misc_parser import parse_misc
from gh_parser import parse_gh
from asset_parser import parse_asset
from docs_parser import parse_docs, parse_docs_options
from deploy_setup import deploy_setup

import copy, os, travispy

parse_misc()

rebuild_yml = {
    "language": ["objective-c"],
    "install": ["sh ./.sauce/travis/unity_install.sh"],
    "script": ["sh ./.sauce/travis/unity_build.sh"],
    "before_deploy": ["sh ./.sauce/travis/pre_deploy.sh"],
    "deploy": [],
    "env": {
        "global": [
            "verbose=%s" % os.environ["verbose"],
            "packagename=%s" % os.environ["packagename"],
            "include_version=%s" % os.environ["include_version"],
            "TRAVIS_TAG=%s" % os.environ["TRAVIS_TAG"]
        ]
    }
}

try:
    os.environ["GH_TOKEN"]
except KeyError:
    gh_token_present = False
else:
    gh_token_present = True

if (os.environ["TRAVIS_PULL_REQUEST"] == "false" and
    os.environ["TRAVIS_TAG"].strip() and
    gh_token_present):
    
    deploy_yml = copy.deepcopy(rebuild_yml)
    
    #grab the user from the repo slug.
    user = os.environ["TRAVIS_REPO_SLUG"].split("/")[0]

    #grab the repo name from the repo slug.
    project = os.environ["TRAVIS_REPO_SLUG"].split("/")[1]

    #grabs the api_token via travispy (it's there, why not use it?) authenticate with the gh token then grab the token from the headers (see TravisPy class)
    api_token = travispy.TravisPy.github_auth(os.environ["GH_TOKEN"])._session.headers['Authorization'].split()[1]
    
    ini_docs = parse_docs()
    if ini_docs:
        deploy_yml["after_success"] = ini_docs
        #deploy_yml["deploy"].append(ini_docs)
        print '------------------------------------------------------------------------------------------------------------------------'
        print "Deployment to Github Pages accepted. -----------------------------------------------------------------------------------"
        print '------------------------------------------------------------------------------------------------------------------------'
        deploy_yml["env"]["global"].extend(parse_docs_options(api_token))
        
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
        deploy_setup(api_token, deploy_yml)
    
else:
    print '------------------------------------------------------------------------------------------------------------------------'
    print "Skipping deployment. ---------------------------------------------------------------------------------------------------"
    print '------------------------------------------------------------------------------------------------------------------------'

#you only get here if there is no deployment since deploy_setup calls exit on success.
if os.environ["always_run"] == "True": #move on to the build steps. This needs to be invoked like this to be able to pass the env vars created here.
    if (os.system("sh ./.sauce/travis/unity_install.sh") == 0 and
        os.system("sh ./.sauce/travis/unity_build.sh") == 0):
        exit(0)
    else:
        exit(1)
else:
    print '------------------------------------------------------------------------------------------------------------------------'
    print "Skipping build steps. ---------------------------------------------------------------------------------------------------"
    print '------------------------------------------------------------------------------------------------------------------------'

