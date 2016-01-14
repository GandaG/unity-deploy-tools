#! /bin/sh

#testing variables
find ./
echo $project
echo $package

echo 'Downloading from http://download.unity3d.com/download_unity/f3d16a1fa2dd/MacEditorInstaller/Unity-5.2.3f1.pkg: '
curl -o CI/Unity.pkg http://download.unity3d.com/download_unity/f3d16a1fa2dd/MacEditorInstaller/Unity-5.2.3f1.pkg

echo 'Installing Unity.pkg'
sudo installer -dumplog -package CI/Unity.pkg -target /
