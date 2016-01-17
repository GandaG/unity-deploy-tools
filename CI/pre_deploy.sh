#! /bin/sh

project="${TRAVIS_REPO_SLUG##*/}"
package=$project.unitypackage

if [ "$project" == "unitypackage-ci" ];
then
   echo "Preparing directories;"
   mkdir ./Temp
   mkdir ./Deploy
   
   #grab everything inside CI/ except the files created during the build.
   echo "Move stuff inside CI/ to Temp/"
   find ./CI/ \ 
    ! -path '*/\.*' \ 
	! -name "*.pkg" \ 
	! -name "*.log" \ 
	! -name ".gitignore" \ 
	-exec mv {} ./Temp/ \; 

   echo "Grab the README and the LICENSE."
   #also grab the readme and the license.
   find ./* \
    -name "README.rst" \
	-name "LICENSE" \
	-exec mv {} ./Temp/ \;
   
   /bin/cat <<EOM > ./Temp/.travis.yml
   language: objective-c
    
   install:
     - sh ./CI/py_set_up.sh
     - python ./CI/deploy_set_up.py
     - sh ./CI/unity_install.sh
    
   script:
     - sh ./CI/unity_build.sh
    
   env:
     global:
       - secure: Gihutb_encrypted_token_here

EOM
   
   #checking the files inside temp - for testing only
   echo "All files inside temp;"
   find ./Temp/*
   
   echo "New yml file:"
   cat ./Temp/.travis.yml
   
   echo "Zip everything up."
   zip ./Temp/* "./Deploy/$project.zip"
else
   mkdir ./Deploy
   
   find ./Project/* \
    -name "$package" \
	-exec zip {} "./Deploy/$project.zip" \;
fi
