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
    
    options = []
    
    projectname = config.get('Docs', 'projectname')
    description = config.get('Docs', 'description')
    logo = config.get('Docs', 'logo')
    
    include_non_documented = config.getboolean('Docs', 'include_non_documented')
    include_privates = config.getboolean('Docs', 'include_privates')
    include_nav_panel = config.getboolean('Docs', 'include_nav_panel')
    include_search = config.getboolean('Docs', 'include_search')
    gen_diagrams = config.getboolean('Docs', 'gen_diagrams')
    
    if projectname:
        options.append("projectname=%s" % projectname)
    
    if description:
        options.append("description=%s" % description)
        
    if logo:
        options.append("logo=%s" % logo)
    
    if include_non_documented:
        options.append("include_non_documented=YES")
    else:
        options.append("include_non_documented=NO")
    
    if include_privates:
        options.append("include_privates=YES")
    else:
        options.append("include_privates=NO")
    
    if include_nav_panel:
        options.append("include_nav_panel=YES")
    else:
        options.append("include_nav_panel=NO")
    
    if include_search:
        options.append("include_search=YES")
    else:
        options.append("include_search=NO")
    
    if gen_diagrams:
        options.append("gen_diagrams=YES")
        options.append("class_diagrams=NO") #this is just the opposite of the dot graphs - I set it to the opposite here just because it's easier than at deployment
    else:
        options.append("gen_diagrams=NO")
        options.append("class_diagrams=YES")
    
    return options

