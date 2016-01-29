#!/usr/bin/env python

import ConfigParser, os

def parse_docs():
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('.sauce.ini')
    
    if not config.getboolean('Docs', 'enable'):
        return None
    
    branch = config.get('Docs', 'branch')
    
    deploy_docs = {
        "provider": "script",
        "script": "sh ./.sauce/travis/deploy_docs.sh",
        "skip_cleanup": "true",
        "on": {}
    }
    
    if branch:
        deploy_docs["on"]["branch"] = branch
    else:
        deploy_docs["on"]["all_branches"] = "true"
        
    return deploy_docs

def parse_docs_options():
    
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('.sauce.ini')
    
    include_non_documented = config.getboolean('Docs', 'include_non_documented')
    include_privates = config.getboolean('Docs', 'include_privates')
    include_nav_panel = config.getboolean('Docs', 'include_nav_panel')
    include_search = config.getboolean('Docs', 'include_search')
    gen_diagrams = config.getboolean('Docs', 'gen_diagrams')
    
    options = [
        "include_non_documented=%s" % include_non_documented,
        "include_privates=%s" % include_privates,
        "include_nav_panel=%s" % include_nav_panel,
        "include_search=%s" % include_search,
        "gen_diagrams=%s" % gen_diagrams,
    ]
    
    projectname = config.get('Docs', 'projectname')
    description = config.get('Docs', 'description')
    logo = config.get('Docs', 'logo')
    
    if projectname:
        options.append("projectname=%s" % projectname)
    
    if description:
        options.append("description=%s" % description)
        
    if logo:
        options.append("logo=%s" % logo)
    
    return options

