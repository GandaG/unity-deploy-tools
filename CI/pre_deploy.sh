#! /bin/sh


if [ $project == "unitypackage-ci" ];
then
   mkdir ./Temp
   mkdir ./Deploy
   
   find ./CI/ \ 
    ! -path '*/\.*' \ 
	! -name "*.pkg" \ 
	! -name "*.log" \ 
	! -name ".gitignore" \ 
	-exec mv {} ./Temp/ \; 
	
   find ./* \
    -name "README.rst"
	-name "LICENSE"
	-exec mv {} ./Temp/ \;
	
   #checking the files inside temp - for testing only
   echo "All files inside temp;"
   find ./Temp/*
   
   /bin/cat <<EOM > ./Temp/.travis.yml
   language: objective-c

   install:
    - sh CI/install.sh
   
   script:
    - sh CI/build.sh
    
   before_deploy:
    - sh CI/pre_deploy.sh
   
   deploy:
     provider: releases
     api_key: 
      secure: $GH_TOKEN_SECURE
     file: ./Deploy/$project.zip
     skip_cleanup: true
     on:
       tags: true
   env:
    - project = "${TRAVIS_REPO_SLUG##*/}"
    - package = $project.unitypackage
    - GH_TOKEN_SECURE = put.encrypted.oauth.gh.token.here
EOM
   
   zip ./Temp/* ./Deploy/$project.zip
else
   mkdir ./Deploy
   
   find ./Project/* \
    -name $package
	-exec zip {} ./Deploy/$project.zip
fi
