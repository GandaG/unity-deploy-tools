#! /bin/sh

project="ci-build"

echo "Attempting to package $project"
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -silent-crashes -logFile $(pwd)/unity.log -exportPackage $(pwd) $(project) -quit

echo 'Logs from package:'
cat $(pwd)/unity.log
