#!/usr/bin/env python

import ConfigParser, os

def parse_gh():
    
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('config.ini')
    
    gh_token = config.get('Github', 'token')
    
    if gh_token is None:
        return None
    
    try: #check if the env already exists, it's better not to mess with existing stuff
        os.environ["gh_token"]
    except KeyError:
        os.environ["gh_token"] = gh_token
    else:
        print "\"gh_token\" already exists as an env variable. change it to something else."
        exit(1)
    
    
    prerelease = config.getboolean('Github', 'prerelease')
    if not prerelease:
        conditional_prerelease = config.getboolean('Github', 'conditional_prerelease')
        if conditional_prerelease and ("alpha" in os.environ["TRAVIS_TAG"] or "beta" in os.environ["TRAVIS_TAG"]):
            prerelease = True
    
    draft = config.getboolean('Github', 'draft')
    if not draft:
        conditional_draft = config.getboolean('Github', 'conditional_draft')
        if conditional_draft and ("alpha" in os.environ["TRAVIS_TAG"] or "beta" in os.environ["TRAVIS_TAG"]):
            draft = True
    
    description = config.get('Github', 'description')
    branch = config.get('Github', 'branch')
    packagename = config.get('Github', 'packagename')
    
    deploy_gh = {
        "provider": "releases",
        "api_key": [{"secure": gh_token}],
        "target_commitish": os.environ["TRAVIS_COMMIT"],
        "name": os.environ["TRAVIS_TAG"],
        "draft": draft,
        "prerelease": prerelease,
        "skip_cleanup": "true"
        "on" : {}
    }
    
    if description:
        deploy_gh["description"] = description
    
    if branch:
        deploy_gh["on"]["branch"] = branch
    else:
        deploy_gh["on"]["all_branches"] = "true"
    
    if packagename:
        deploy_gh["file"] = "./Deploy/%s.zip" % packagename
    else:
        deploy_gh["file"] = "./Deploy/%s.zip" % os.environ["TRAVIS_REPO_SLUG"].split("/")[1] #this is the repo name
    
    return deploy_gh

    