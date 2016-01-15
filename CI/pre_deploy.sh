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

   before_install:
     - pip install requests
     - python ./CI/set_up.py
   
   install:
     - sh CI/install.sh
   
   script:
     - sh CI/build.sh
     
   env:
     global:
       - secure: API_encrypted_token_here
       - secure: Gihutb_encrypted_token_here

EOM
   
   zip ./Temp/* "./Deploy/$project.zip"
else
   mkdir ./Deploy
   
   find ./Project/* \
    -name "$package" \
	-exec zip {} "./Deploy/$project.zip" \;
fi
