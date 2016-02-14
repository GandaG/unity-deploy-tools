#!/usr/bin/env python

import ConfigParser, os

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

def parse_unity_versions():
    
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('.deploy.ini')
    
    unity_vers = config.get('Misc', 'unity_versions')
    
    if not unity_vers:
        return ["5.0.1"] #once/if a scraper is written this should return the latest version.
    
    return unity_vers.split()
    
def get_available_unity_vers():
    
    #once/if a scraper is written, this should output the scraper's results instead of a fixed list.
    version_dict = {
        "5.0.1": "http://download.unity3d.com/download_unity/5a2e8fe35a68/MacEditorInstaller/Unity-5.0.1f1.pkg",
        "5.0.2": "http://download.unity3d.com/download_unity/0b02744d4013/MacEditorInstaller/Unity-5.0.2f1.pkg",
        "5.0.3": "http://download.unity3d.com/download_unity/c28c7860811c/MacEditorInstaller/Unity-5.0.3f2.pkg",
        "5.0.4": "http://download.unity3d.com/download_unity/1d75c08f1c9c/MacEditorInstaller/Unity-5.0.4f1.pkg",
        "5.1.0": "http://download.unity3d.com/download_unity/ec70b008569d/MacEditorInstaller/Unity-5.1.0f3.pkg",
        "5.1.1": "http://download.unity3d.com/download_unity/2046fc06d4d8/MacEditorInstaller/Unity-5.1.1f1.pkg",
        "5.1.2": "http://download.unity3d.com/download_unity/afd2369b692a/MacEditorInstaller/Unity-5.1.2f1.pkg",
        "5.1.3": "http://download.unity3d.com/download_unity/b0a23b31c3d8/MacEditorInstaller/Unity-5.1.3f1.pkg",
        "5.1.4": "http://download.unity3d.com/download_unity/36d0f3617432/MacEditorInstaller/Unity-5.1.4f1.pkg",
        "5.2.0": "http://download.unity3d.com/download_unity/e7947df39b5c/MacEditorInstaller/Unity-5.2.0f3.pkg",
        "5.2.1": "http://download.unity3d.com/download_unity/44735ea161b3/MacEditorInstaller/Unity-5.2.1f1.pkg",
        "5.2.2": "http://download.unity3d.com/download_unity/3757309da7e7/MacEditorInstaller/Unity-5.2.2f1.pkg",
        "5.2.3": "http://download.unity3d.com/download_unity/f3d16a1fa2dd/MacEditorInstaller/Unity-5.2.3f1.pkg",
        "5.2.4": "http://download.unity3d.com/download_unity/98095704e6fe/MacEditorInstaller/Unity-5.2.4f1.pkg",
        "5.3.0": "http://download.unity3d.com/download_unity/2524e04062b4/MacEditorInstaller/Unity-5.3.0f4.pkg",
        "5.3.1": "http://download.unity3d.com/download_unity/cc9cbbcc37b4/MacEditorInstaller/Unity-5.3.1f1.pkg",
        "5.3.2": "http://netstorage.unity3d.com/unity/e87ab445ead0/MacEditorInstaller/Unity-5.3.2f1.pkg"
    }
    
    return version_dict


