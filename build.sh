#! /bin/sh

project="ci-build"

echo "Setting up project directory:"
mkdir $(pwd)/Project
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
-batchmode \
-nographics \
-silent-crashes \
-logFile $(pwd)/unityProject.log \
-createProject $(pwd)/Project \
-quit

echo "Move files to Assets/"
mkdir $(pwd)/Project/Assets/$project
for file in $(pwd)/*
do
  if [ $file != "Project" -o $file != "install.sh" -o $file != "Unity.pkg" -o $file != "unityProject.log" -o $file != "build.sh" ]
  then
    mv $file $(pwd)/Project/Assets/$project/
  fi
done

echo "Attempting to package $project:"
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
-batchmode \
-nographics \
-silent-crashes \
-logFile $(pwd)/unityPackage.log \
-projectPath $(pwd)/Project \
-exportPackage $(pwd)/Project/Assets/$project $project \
-quit

echo 'Logs from package:'
cat $(pwd)/unityProject.log
cat $(pwd)/unityPackage.log
