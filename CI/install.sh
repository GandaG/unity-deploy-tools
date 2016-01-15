#! /bin/sh

#the only case where it shouldn't run is if there is an api key present but it's not rebuilding.
if ! [ -z "${API_TOKEN+x}" ];
then
	if [ -z "${REBUILDING+x}" ];
	then exit 0
	fi
fi

echo 'Downloading Unity;'
curl -o CI/Unity.pkg http://download.unity3d.com/download_unity/f3d16a1fa2dd/MacEditorInstaller/Unity-5.2.3f1.pkg

echo 'Installing Unity;'
sudo installer -dumplog -package CI/Unity.pkg -target /
