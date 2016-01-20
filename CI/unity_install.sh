#! /bin/sh

#the only case where it shouldn't run is if there is an api key present but it's not rebuilding.
if [ ! -z "$TRAVIS_TAG" -a "$TRAVIS_TAG" != " " ];
then
    if ! [ -z "${GH_TOKEN+x}" ];
    then
        if [ -z "${REBUILDING+x}" ];
        then exit 0
        fi
    else
        if ! [ -z "${ASSET_TOKEN+x}" ];
        then
            if [ -z "${REBUILDING+x}" ];
            then exit 0
            fi
        fi
    fi
fi

printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
echo 'Downloading Unity; -----------------------------------------------------------------------------------------------------'
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
curl -o CI/Unity.pkg http://download.unity3d.com/download_unity/f3d16a1fa2dd/MacEditorInstaller/Unity-5.2.3f1.pkg

printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
echo 'Installing Unity; ------------------------------------------------------------------------------------------------------'
printf '%s\n' ------------------------------------------------------------------------------------------------------------------------
sudo installer -dumplog -package CI/Unity.pkg -target /
