.. image:: https://travis-ci.org/GandaG/unitypackage-ci.svg?branch=master
    :target: https://travis-ci.org/GandaG/unitypackage-ci

###############
unitypackage-ci
###############
*Continuous integration for open-source* `Unity3D <https://unity3d.com/>`_ *packages and assets.*

This repo offers a quick way to setup open source unity packages. As of the latest commit it offers automated package exporting an deployment to Github. More features are planned.



***************
Installation
***************
1. Download the `latest stable release <https://github.com/GandaG/unitypackage-ci/releases/latest>`_;

2. Unpack the files into your repository's root directory;

3. Go to `Travis-CI <https://travis-ci.org/>`_ an sign in with Github;

4. Enable your repository in your account page;

5. For additional features check the subsections below;

6. Simply push a commit and let travis do all the work for you!

Github Releases
""""""""""""""""""
To enable deployment to Github Releases:

1. Sign in to Github;

2. Go to your `Settings <https://github.com/settings/>`_;

3. Go to `Personal Access Tokens <https://github.com/settings/tokens>`_;

4. Click on :code:`Generate new token`;

5. Enter your password;

6. Give the token a good description. Mine is :code:`Travis-CI Deploy`;

7. Give the token these permissions:

   - gist;
   - read:org; 
   - repo; 
   - user:email;
   - write:repo_hook

8. Click on :code:`Generate token`;

9. The new token should now appear. NEVER give or show this token to anyone, not even Travis (the encryption process later on does not send the token to Travis, the entire process is local);

10. Temporarily store your token somewhere local and safe;

11. If you're using OSX or Linux/Unix feel free to skip this part. This is for Windows users who don't have Ruby installed:

    1. Install Ruby via `RubyInstaller <http://rubyinstaller.org/downloads/>`_; 

    2. Download the Development Kit from the same download page as Ruby Installer. Choose the .exe file corresponding to your environment (32 bits or 64 bits and working with your version of Ruby).

    3. Follow the `installation instructions <https://github.com/oneclick/rubyinstaller/wiki/Development-Kit>`_ for DevelopmentKit.

12. On your terminal/command line, run :code:`gem install travis`;

13. Run :code:`travis encrypt GH_TOKEN=place_your_token_here -r your_username/your_repo_name`. Substitute your info in the proper places.

14. Copy everything after :code:`secure:` to the proper place in the .travis.yml file (should be about 600 random characters);

15. Commit the change and every time you push a tag Travis will deploy to Github!

16. If you're not using any other feature it's now safe to delete and forget about that token from before! Only use the secure (encrypted) version from now on.

*****************
Upcoming Features
*****************
- Automated package deployment to `Unity <https://unity3d.com/>`_'s Asset Store.
- Automated documentation generation.