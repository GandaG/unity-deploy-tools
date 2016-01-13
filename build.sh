#! /bin/sh

project="ci-build"

echo "Setting up project directory;"
mkdir ./Project
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile ./unityProject.log \
 -createProject ./Project \
 -quit

echo "Moving files into temporary project;"
mkdir -p ./Project/Assets/$project

find ./* \
 ! -path '*/\.*' \
 ! -path ./Project/ \
 ! -path ./.git/ \
 ! -name "*.sh" \
 ! -name "*.pkg" \
 ! -name "*.log" \
 ! -name ".gitignore" \
 -print
# -exec mv {} ./Project/Assets/$project/ \;

echo "Attempting to package $project;"
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile ./unityPackage.log \
 -projectPath "$PWD"/Project \
 -exportPackage ./Project/Assets/$project $project \
 -quit

echo 'Logs from package:'
cat ./unityProject.log
cat ./unityPackage.log
