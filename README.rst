.. |travisbadge| image:: https://travis-ci.org/GandaG/unity-deploy-tools.svg?branch=master
    :target: https://travis-ci.org/GandaG/unity-deploy-tools

.. |nbsp| unicode:: 0xA0 
   :trim:

####################################################################################
Unity Deployment Tools |nbsp| |nbsp| |nbsp| |travisbadge|
####################################################################################
*Continuous deployment tools for open-source* `Unity3D <https://unity3d.com/>`_ *packages and assets.*

********
Overview
********

.. _.ini: .deploy.ini

.. _all the options: `Configuration`_

Unity Deployment Tools offers a quick way to setup open source unity packages. It features:

- a self-documented and easy to use `.ini`_ file to configure `all the options`_;
- automated package/asset exporting from unity;
- automated deployment to Github Releases;
- automated creation and deployment of documentation to Github Pages.

Projects using UDT
""""""""""""""""""

.. _UnitySteer: https://github.com/ricardojmendez/UnitySteer

- `UnitySteer`_

************
Installation
************

.. _.deploy.ini: .deploy.ini

1. Download the `latest stable release <https://github.com/GandaG/unitypackage-ci/releases/latest>`_;

2. Unpack the files into your repository's root directory;

3. Go to `Travis-CI <https://travis-ci.org/>`_ an sign in with Github;

4. Enable your repository in your account page;

5. Open `.deploy.ini`_ with a text editor (like Notepad++) and modify the options under the :code:`[Misc]` section as per your preferences.

6. For additional `features`_ check the subsections below;

7. Simply push a commit and let travis do all the work for you!

Once you're using UDT please consider `leaving a comment <https://github.com/GandaG/unity-deploy-tools/issues>`_ so that I can add your repo 
to the list__!

__ `Projects using UDT`_

*******************
Features
*******************
These tools are all targeted at the majority of Unity users: the newbies. While more advanced users will also find them useful 
(automation is always welcome) everything by default is as simple as possible to configure (a simple `.ini`_ file) and to 
use (unzip and copy to your repo).

Some features have requirements (e.g. having a tag associated with the commit) which you have to fulfill before using them. The 
only exception is the automated building and exporting of the package (this includes no deployment/upload - it is simply to check
is the package CAN be built and exported correctly). These requirements are shown at the beggining of each feature description.


Github Releases
""""""""""""""""""
- Requirements
    - `Github OAuth Token`_ present;
    - Tag present;
    - Not on a Pull Request.

Simply open your `.deploy.ini`_ file with a text editor (like Notepad++) and modify the :code:`[Github]` 
section as per your preferences. That's it, really.

Code Documentation
""""""""""""""""""
- Requirements
    - `Github OAuth Token`_ present;
    - Tag present;
    - Not on a Pull Request.

Documentation for all your code is generated with `Doxygen <http://www.stack.nl/~dimitri/doxygen/index.html/>`_.
Example documentation is provided at the `Github Pages <https://gandag.github.io/unity-deploy-tools/>`_ of this repository, 
example script taken from Microsoft's `XML Documentation Example <https://msdn.microsoft.com/en-us/library/aa288481(v=vs.71).aspx>`_.

Basic Usage
'''''''''''
Documentation generation is enabled by default. Open your `.deploy.ini`_ file with a text editor (like Notepad++) 
and modify the :code:`[Docs]` section as per your preferences. That's pretty much it, for more things to do with Doxygen check below.

Advanced/Expert
'''''''''''''''

.. _Doxyfile: .deploy/docs/Doxyfile

.. _deploy_docs.sh: .deploy/travis/deploy_docs.sh

Doxygen must be (for the sheer amount of options) the best documented software I've ever seen. 

If you want to customize your docs more than the basic options presented in the `.deploy.ini`_ file 
(these are the same presented in the basic panel of the doxywizard)
open the `Doxyfile`_. This is the default doxygen configuration file and every option is very well 
documented. There are bajillions of them, have fun!

Please note that some options are hardcoded (see `deploy_docs.sh`_).

*****************
Known Issues
*****************
- Build error due to timeout on Travis-CI.
    ``No fix available`` - Sometimes the connection speed from the Travis-CI worker to the unity servers is 
    just too slow and the build times out. No fix unless Travis somehow allows us to restart the build automatically.

    ``Workaround`` - Simply restart the build until the connection is faster. 


*****************
Upcoming Features
*****************
- Automated compiling and distribution as a .dll file.

******
Extras
******

Configuration
"""""""""""""
| These are all the options present in the `.ini`_ file.

.. note:: ``None`` corresponds to an empty field.

Misc Section
''''''''''''
- verbose
    - Default:
        ``false``
    - If set to true, all logs from commands will be shown.
- always_run
    - Default:
        ``true``
    - If set to true, Travis will always try to build the package/asset, even when there isn't a tag. 
- unity_version
    - Default:
        ``None``
    - Place the unity version you wish to build againts here (e.g. unity_version=5.1.0). See supported versions in the readme. If none are specified, version 5.0.1 (the earliest supported) is used.

Docs Section
''''''''''''
- enable
    - Default:
        ``true``
    - If set to true, will enable generating docs and deploying them to github pages.

- branch
    - Default:
        ``master``
    - If you want to generate documentation only from a specific branch.

- projectname
    - Default:
        ``None``
    - If you want to name your project something other than the repo name.

- username
    - Default:
        ``None``
    - If you want to have a custom username when pushing to gh-pages, fill in. If left blank, defaults to "Travis-CI Doxygen Deployment".

- email
    - Default:
        ``None``
    - If you want to have a custom email when pushing to gh-pages, fill in. If left blank, defaults to "doxygen@deployment.to.github.pages".

- commit_description
    - Default:
        ``None``
    - If you want to have a custom message for the commit to gh-pages, fill in. If left blank, defaults to "Deploying to GitHub Pages".

- description
    - Default:
        ``None``
    - If you want the short description to be something other than your repo description.

- include_version
    - Default:
        ``false``
    - If set to true, will include the tag as the documentation version.

- logo
    - Default:
        ``None``
    - If you wish your project to have a logo, fill in the relative path to the image.(e.g. if you store it in the .deploy folder, fill in this: ./.deploy/my_logo.png)

- include_non_documented
    - Default:
        ``true``
    - If set to true, will include all code even if not documented.

- include_privates
    - Default:
        ``true``
    - If set to true, will include private members in the documentation.

- include_nav_panel
    - Default:
        ``true``
    - If set to true, will include a sidebar with a navigation panel.

- include_search
    - Default:
        ``true``
    - If set to true, will include a search function in each page.

- gen_diagrams
    - Default:
        ``true``
    - If set to true, will generate class hierarchy diagrams.
    
Github Section
''''''''''''''
- enable
    - Default:
        ``true``
    - If set to true, will enable deployment to github if possible.

- include_version
    - Default:
        ``true``
    - If set to true, tag will be included after the package name (e.g. UnityDeployTools_v1.1).

- packagename
    - Default:
        ``None``
    - If you want to name the deploy zip file something other than your repo name.

- conditional_deployment
    - Default:
        ``true``
    - If set to true, tags with "alpha" or "beta" in their name will be deployed.

- conditional_prerelease
    - Default:
        ``true``
    - If set to true, tags with "alpha" or "beta" in their name will be set to prerelease.

- conditional_draft
    - Default:
        ``false``
    - If set to true, tags with "alpha" or "beta" in their name will be deployed as draft.

- conditional_description
    - Default:
        ``None``
    - If filled in, tags with "alpha" or "beta" in their name will have this description. (don't forget this should be in github markdown)

- prerelease
    - Default:
        ``false``
    - If set to true, releases will always be set to prerelease. Overrides conditional_prerelease if true.

- draft
    - Default:
        ``false``
    - If set to true, releases will always be deployed as a draft. Overrides conditional_draft if true.

- title
    - Default:
        ``None``
    - If you want to name the release something other than the tag.

- description
    - Default:
        ``None``
    - If you want to add something to the release description. (don't forget this should be in github markdown) 

- branch
    - Default:
        ``None``
    - If you want to deploy only from a specific branch.


Github OAuth Token
""""""""""""""""""
1. Sign in to Github;

2. Go to your `Settings <https://github.com/settings/>`_;

3. Go to `Personal Access Tokens <https://github.com/settings/tokens>`_;

4. Click on :code:`Generate new token`;

5. Enter your password;

6. Give the token a good description. Mine is :code:`Travis-CI Unity Deploy Tools`;

7. Give the token these permissions:

   - gist;
   - read:org; 
   - repo; 
   - user:email;
   - write:repo_hook

8. Click on :code:`Generate token`;

9. The new token should now appear. NEVER give or show this token to anyone, not even Travis (the encryption process later on does not send the token to Travis, the entire process is local);

10. Temporarily store your token somewhere local and safe;

11. Go to `Travis-CI <https://travis-ci.org/>`_ and sign in with Github;

12. Go to your repository settings;

13. In the Environment Variables section, write "GH_TOKEN" (without the quotes) in the :code:`Name` field and paste the token in the :code:`Value` field;

14. Make sure to leave :code:`Display value in build log` as :code:`OFF` and click :code:`Add`;

15. It's now safe to delete and forget about that token from before! Only use the secure (encrypted) version from now on.

Supported Unity Versions
"""""""""""""""""""""""""""

.. _unity_supported_versions.json: .deploy/travis/unity_supported_versions.json

- 5.0.1 
- 5.0.2
- 5.0.3
- 5.0.4
- 5.1.0
- 5.1.1
- 5.1.2
- 5.1.3
- 5.1.4
- 5.2.0
- 5.2.1
- 5.2.2
- 5.2.3
- 5.2.4
- 5.3.0
- 5.3.1
- 5.3.2

Earlier versions are not supported. If a new version has come out and it isn't yet supported, you can follow these instructions to add it:

- `Set up Git <https://help.github.com/articles/set-up-git/>`_;
- `Fork and clone this repo <https://help.github.com/articles/fork-a-repo/>`_;
- `Create a branch <https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/>`_ and commit your fixes in it:
    - Open the `unity_supported_versions.json`_ file with a text editor;
    - Get the download link to the version you want to add;
        - Make sure the link refers to the Mac Unity Editor;
        - Make sure the link ends in ``.pkg``  -  ``.dmg`` links are not supported.
    - Add the new version to the dictionary like this:
        .. code-block:: json

            {
                "5.0.1": "http://download.unity3d.com/download_unity/5a2e8fe35a68/MacEditorInstaller/Unity-5.0.1f1.pkg",
                "5.0.2": "http://download.unity3d.com/download_unity/0b02744d4013/MacEditorInstaller/Unity-5.0.2f1.pkg",
                "5.0.3": "http://download.unity3d.com/download_unity/c28c7860811c/MacEditorInstaller/Unity-5.0.3f2.pkg",
                "5.0.4": "http://download.unity3d.com/download_unity/1d75c08f1c9c/MacEditorInstaller/Unity-5.0.4f1.pkg",
                "5.1.0": "http://download.unity3d.com/download_unity/ec70b008569d/MacEditorInstaller/Unity-5.1.0f3.pkg",
                "new.unity.version": "http://unity.editor.download.link.for.mac.pkg"
            }
- Push your local branch to your fork;
- `Create a Pull Request <https://help.github.com/articles/using-pull-requests/>`_ to this fork.
