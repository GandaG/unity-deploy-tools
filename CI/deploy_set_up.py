import requests
import travispy
import os

if os.environ["TRAVIS_PULL_REQUEST"] != "false":
    print '------------------------------------------------------------------------------------------------------------------------'
    print "On pull request, skipping deployment. ----------------------------------------------------------------------------------"
    print '------------------------------------------------------------------------------------------------------------------------'
    exit(0) #It's better to not rebuild on pr since the secure variables are not shared.

if not os.environ["TRAVIS_TAG"].strip():
    print '------------------------------------------------------------------------------------------------------------------------'
    print "No tag pushed, skipping deployment. ------------------------------------------------------------------------------------"
    print '------------------------------------------------------------------------------------------------------------------------'
    exit(0) #travis for some reason doesn't check for tags when rebuilding.

try:
    os.environ["GH_TOKEN"] #check if there is an api token. If not, skip rebuild and deployment.
except KeyError:
    try:
        os.environ["ASSET_TOKEN"] #not supported for now but hopefully somewhere in the future.
    except KeyError:
        print '------------------------------------------------------------------------------------------------------------------------'
        print "No deployment tokens found. Skipping deployment. -----------------------------------------------------------------------"
        print '------------------------------------------------------------------------------------------------------------------------'
        exit(0)

print '------------------------------------------------------------------------------------------------------------------------'
print "Deployment token(s) found. Starting deployment. ------------------------------------------------------------------------"
print '------------------------------------------------------------------------------------------------------------------------'

#grab the user from the repo slug.
user = os.environ["TRAVIS_REPO_SLUG"].split("/")[0]

#grab the repo name from the repo slug.
project = os.environ["TRAVIS_REPO_SLUG"].split("/")[1]

#the url to request to: not that instead of a '/' like in the slug, a '%2F' is required here.
url = "https://api.travis-ci.org/repo/" + user + "%2F" + project + "/requests"

#grabs the api_token via travispy (it's there, why not use it?) authenticate with the gh token then grab the token from the headers (see TravisPy class)
api_token = travispy.TravisPy.github_auth(os.environ["GH_TOKEN"])._session.headers['Authorization'].split()[1]

#the headers required by travis. see: https://docs.travis-ci.com/user/triggering-builds
headers = {"Content-Type": "application/json",
            "User-Agent": "UnityPackageAssist/0.0.0",
            "Accept": "application/vnd.travis-ci.2+json",
            "Travis-API-Version": "3",
            "Authorization": "token %s" % api_token}

#the new yml file. it only overrides sections it uses, the rest is from the original. Be careful when editing this.
baseymldict = {"language": ["objective-c"],
                "install": ["sh ./CI/unity_install.sh"],
                "script": ["sh ./CI/unity_build.sh"],
                "before_deploy": ["sh ./CI/pre_deploy.sh"],
                "env": {"global": ["REBUILDING = true"]}
                }

#the json request. token is here again just to be sure but probably isn't needed.
requestdict = {"message": "Deployment requested. Rebuilding.",
                "branch": os.environ["TRAVIS_BRANCH"],
                "token": api_token,
                "config": baseymldict}

#nested dicts are confusing, this lets me think properly <.<
json = {"request": requestdict}



#checking the variables exist to append their deploy to the list. Needs to be fixed when adding support to asset store.
try:
    os.environ["GH_TOKEN"]
except KeyError:
    print '------------------------------------------------------------------------------------------------------------------------'
    print "Github token not found. Not deploying to Github Releases. --------------------------------------------------------------"
    print '------------------------------------------------------------------------------------------------------------------------'
else:
    print '------------------------------------------------------------------------------------------------------------------------'
    print "Github token found. Deploying to Github Releases. ----------------------------------------------------------------------"
    print '------------------------------------------------------------------------------------------------------------------------'
    #the github deploy section.
    deploy_gh = [
        {
        "provider": "releases",
        "api_key": os.environ["GH_TOKEN"],
        "file": "./Deploy/%s.zip" % project,
        "target_commitish": os.environ["TRAVIS_COMMIT"],
        "name": os.environ["TRAVIS_TAG"],
        "draft": True,
        "skip_cleanup": "true",
        }
    ]
    #Add a pre-release check if the tag has the words alpha or beta. Useful but should be able to be turned off.
    if "alpha" in os.environ["TRAVIS_TAG"] or "beta" in os.environ["TRAVIS_TAG"]:
        deploy_gh[0]["prerelease"] = True
    baseymldict["deploy"] = deploy_gh

response = requests.post(url, headers=headers, json=json)

if response.status_code == 202:
    print '------------------------------------------------------------------------------------------------------------------------'
    print "Request accepted by Travis-CI. Rebuilding... ---------------------------------------------------------------------------"
    print '------------------------------------------------------------------------------------------------------------------------'
    exit(0)

if response.status_code != requests.codes.ok:
    print '------------------------------------------------------------------------------------------------------------------------'
    print "Response status code: %s" % response.status_code
    print '------------------------------------------------------------------------------------------------------------------------'
    print "Response history: %s" % response.history
    print '------------------------------------------------------------------------------------------------------------------------'
    raise response.raise_for_status()



