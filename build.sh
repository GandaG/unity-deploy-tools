#! /bin/sh

project="${TRAVIS_REPO_SLUG##*/}"
package=$project.unitypackage

echo "Setting up project directory;"
mkdir ./Project
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile ./unityProject.log \
 -createProject ./Project \
 -quit

echo 'Log:'
cat ./unityProject.log
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------

echo "Moving files into temporary project;"
mkdir -p ./Project/Assets/$project
find ./* \
 ! -path '*/\.*' \
 ! -path "./Project/*" \
 ! -name "Project" \
 ! -name "*.sh" \
 ! -name "*.pkg" \
 ! -name "*.log" \
 ! -name ".gitignore" \
 -exec mv {} ./Project/Assets/$project/ \;

echo "Attempting to package $project;"
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile ./unityPackage.log \
 -projectPath "$PWD"/Project \
 -exportPackage Assets/$project $package \
 -quit

echo 'Log:'
cat ./unityPackage.log
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------

#For testing: I need to know where the package is exported to. The package is exported to ./Project/$package
echo "Unity Package:"
find . -name "*.unitypackage"
