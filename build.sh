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
#find "$(pwd)" \( -type d \( -path "$(pwd)"/Project/ -o -path "$(pwd)"/.git/ \) \
# -o -type f \( -name "*.sh" -o -name "*.pkg" -o -name "*.log" -o -name ".gitignore" \) \) \
# -prune -o \
# \( -type f -o -type d \) \
# -exec mv {} "$(pwd)"/Project/Assets/$project/ \;
 
find . \
 ! -path ./Project/ \
 ! -path ./.git/ \
 ! -name "*.sh" \
 ! -name "*.pkg" \
 ! -name "*.log" \
 ! -name ".gitignore" \
 -type f \
 -exec mv {} ./Project/Assets/$project/ \;

echo "Attempting to package $project;"
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile ./unityPackage.log \
 -projectPath ./Project \
 -exportPackage ./Project/Assets/$project $project \
 -quit

echo 'Logs from package:'
cat ./unityProject.log
cat ./unityPackage.log
