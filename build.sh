#! /bin/sh

project="ci-build"

mkdir $(pwd)/$(project)
shopt -s extglob
mv !($(project)) $(project) #unity packaging api only works with folders so it's simpler to just put it all into one.

echo "Attempting to package $project"
/Applications/Unity/Unity.app/Contents/MacOS/Unity \
  -batchmode \
  -nographics \
  -silent-crashes \
  -logFile $(pwd)/unity.log \
  -projectPath $(pwd) \
  -exportPackage $(pwd)/$(project) package
  -quit

echo 'Logs from package'
cat $(pwd)/unity.log
