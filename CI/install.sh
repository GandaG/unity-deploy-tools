#! /bin/sh

#testing variables
gh_token_secure=AJ21PfMGMhy2VTt3JtOaRtxgD4I/mD8Bvncoeka5hFGv6URzppNAwNBdiE37DQgmMY0AWTL3qQkp9gRoNwWQIOVCaELhR9lqaEkzvyHgjfyooqD/YuLohKusD0W0rITXjgykM2/DFZPuRrIsXI5sUhi5xRkBwPThmK6QeYcKQ9/hwX+twHgDkr+zO4UeN+llcatoFsFEv9X18meBWaUPXMgE4NIoNrcesvMfU8FWVtpMxvM7ZZvWVV2vgyWB6cRP13JPEBfOac+LRUbFqnqxrya7GPsYKYnq0dra7tZmcu5uFXqSMEwi7EKEOybqXSzm+gxC1uGtXj4ycm1RSXNywb05cbuSi4TUTyFJsp2XfOcy0gmdX45ZNFG+2aDayuTn2zHqqkh4DQuh9MDfvNmecZT3ki0S4SHXDMxAbGI/tvarvWiiNC15u7RtISb7i8TiMlfqdaqwoDprpT+ys+1lcHiV31dBm3wIyVH0CXJKMC5EBsfcOy0s1HKtgSpOdOU1wZUL/pQ/XcdHMsulAJOgQKzrOWfok3Qb+mqP9zXYuaZEsA6BpLeUPYC+m+A4GPrptfLclq7ESjwGCy49B8V1ZMLIReBWyXWXJRxWO50ez+pwfNGdvYwOfHB/NtJof2Ifb6r9vc+xiwUisMyFpwWlmemNHeMdcL2XMfRLRYYPAIM=
project="${TRAVIS_REPO_SLUG##*/}"
package=$project.unitypackage
echo "deploy:
  provider: releases
  api_key: 
   secure: $gh_token_secure
  file: ./Deploy/$project.zip
  skip_cleanup: true
  on:
    tags: true
env:
 global:
  - project = $project
  - package = $package
  - gh_token_secure = $gh_token_secure" >> ./.travis.yml
cat ./.travis.yml

echo 'Downloading from http://download.unity3d.com/download_unity/f3d16a1fa2dd/MacEditorInstaller/Unity-5.2.3f1.pkg: '
curl -o CI/Unity.pkg http://download.unity3d.com/download_unity/f3d16a1fa2dd/MacEditorInstaller/Unity-5.2.3f1.pkg

echo 'Installing Unity.pkg'
sudo installer -dumplog -package CI/Unity.pkg -target /
