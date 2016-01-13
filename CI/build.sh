#! /bin/sh

project="${TRAVIS_REPO_SLUG##*/}"
package=$project.unitypackage

echo "Setting up project directory; -------------------------------------------------------------------------------------------------"
mkdir ./Project
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile ./CI/unityProject.log \
 -createProject ./Project \
 -quit

echo 'Project Log; ------------------------------------------------------------------------------------------------------------------'
cat ./CI/unityProject.log
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------

echo "Moving files into temporary project; ------------------------------------------------------------------------------------------"
mkdir -p ./Project/Assets/$project
find ./* \
 ! -path '*/\.*' \
 ! -path "./Project/*" \
 ! -name "Project" \
 ! -path "./CI/*" \
 ! -name "CI" \
 ! -name ".gitignore" \
 -exec mv {} ./Project/Assets/$project/ \;

echo "Attempting to package $project; -----------------------------------------------------------------------------------------------"
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
 -batchmode \
 -nographics \
 -silent-crashes \
 -logFile ./CI/unityPackage.log \
 -projectPath "$PWD"/Project \
 -exportPackage Assets/$project $package \
 -quit

echo 'Packaging Log; ----------------------------------------------------------------------------------------------------------------'
cat ./CI/unityPackage.log
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------

#The package is exported to ./Project/$package
echo "Checking package exists; ------------------------------------------------------------------------------------------------------"
file=find . -name "*.unitypackage" -exec basename {} \;

if [ -e $file ];
then
   exit 0
else
   exit 1
fi
