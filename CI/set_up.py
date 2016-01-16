import requests
import os

try:
	os.environ["API_TOKEN"] #check if there is an api token. If not, skip rebuild and deployment.
except KeyError:
	print "API token not found. Skipping deployment."
	exit(0)
else:
	print "API token found. Starting deployment."

if os.environ["TRAVIS_PULL_REQUEST"] != "false":
	exit(0) #It's better to not rebuild on pr since the secure variables are not shared.

project = os.environ["TRAVIS_REPO_SLUG"].split("/")[1]

package = "%s.unitypackage" % project

url = "https://api.travis-ci.org/repo/%s/requests" % os.environ["TRAVIS_REPO_SLUG"]

branch = os.environ["TRAVIS_BRANCH"]

headers = {"Content-Type": "application/json",
			"Accept": "application/json",
			"Travis-API-Version": "3",
			"Authorization": "token %s" % os.environ["API_TOKEN"]}

baseymldict = {"language": ["objective-c"],
				"before_install": ["sh CI/install.sh"],
				"script": ["sh CI/build.sh"],
				"before_deploy": ["sh CI/pre_deploy.sh"],
				"env": {"global": ["REBUILDING = true"]}
				}

#it would great if the specific commit could be specified
requestdict = {"message": "Testing API requests. Rebuilding with different yml file.",
				"branch": branch,
				"config": baseymldict}

json = {"request": requestdict}

try:
	os.environ["GH_TOKEN"]
except KeyError:
	print "Github token not found. Not deploying to Github Releases."
else:
	print "Github token found. Deploying to Github Releases."
	deploy_gh = [
			{
			"provider": "releases",
			"api_key": [
				{
				"secure": os.environ["GH_TOKEN"]
				}
			],
			"file": "./Deploy/%s.zip" % project,
			"skip_cleanup": "true",
			"on": {
				"tags": "true"
			}
			}
		]
	baseymldict["deploy"] = deploy_gh

response = requests.post(url, headers=headers, json=json)

if response.status_code != requests.codes.ok:
	print "Response content: %s" % response.content
	print "Response status code: %s" % response.status_code
	print "Response history: %s" % response.history
	print "Post request failed, retrying..."
	r2 = requests.post(url, headers=headers, json=json)
	if r2.status_code != requests.codes.ok:
		print "Response content: %s" % r2.content
		print "Response status code: %s" % r2.status_code
		print "Response history: %s" % r2.history
		raise r2.raise_for_status()
		exit(1)
	else:
		print r2.content
else:
	print response.content



