#! /bin/sh

project="ci-build"

echo "Setting up project directory;"
mkdir "$(pwd)"/Project
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile "$(pwd)"/unityProject.log \
 -createProject "$(pwd)"/Project \
 -quit

echo "Moving files into temporary project;"
mkdir -p "$(pwd)"/Project/Assets/$project
find "$(pwd)" \
 -path "$(pwd)"/Project/ \
 -a -path "$(pwd)"/.git/ \
 -a -name "*.sh" \
 -a -name "*.pkg" \
 -a -name "*.log" \
 -a -name ".gitignore" \
 -prune -o \
 -name "*" \
 -exec mv {} "$(pwd)"/Project/Assets/$project/ \;

echo "Attempting to package $project;"
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile "$(pwd)"/unityPackage.log \
 -projectPath "$(pwd)"/Project \
 -exportPackage "$(pwd)"/Project/Assets/$project $project \
 -quit

echo 'Logs from package:'
cat "$(pwd)"/unityProject.log
cat "$(pwd)"/unityPackage.log
