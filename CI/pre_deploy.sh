#! /bin/sh

project="${TRAVIS_REPO_SLUG##*/}"
package=$project.unitypackage

if [ "$project" == "unitypackage-ci" ];
then
   mkdir ./Temp
   mkdir ./Deploy
   
   #grab everything inside CI/ except the files created during the build.
   find ./CI/ \ 
    ! -path '*/\.*' \ 
	! -name "*.pkg" \ 
	! -name "*.log" \ 
	! -name ".gitignore" \ 
	-exec mv {} ./Temp/ \; 

   #also grab the readme and the license.
   find ./* \
    -name "README.rst" \
	-name "LICENSE" \
	-exec mv {} ./Temp/ \;
	
   #checking the files inside temp - for testing only
   echo "All files inside temp;"
   find ./Temp/*
   
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
   
   echo "New yml file:"
   cat ./Temp/.travis.yml
   
   zip ./Temp/* "./Deploy/$project.zip"
else
   mkdir ./Deploy
   
   find ./Project/* \
    -name "$package" \
	-exec zip {} "./Deploy/$project.zip" \;
fi
