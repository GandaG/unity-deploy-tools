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
mv $(pwd)/* $(pwd)/Project/Assets/$project
rm -r $(pwd)/Project/Assets/$project/Project

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
