import requests

print TRAVIS_PULL_REQUEST

try:
	API_TOKEN #check if there is an api token. If not, skip rebuild and deployment.
except NameError:
	print "API token not found. Skipping deployment."
	exit(0)

if TRAVIS_PULL_REQUEST != "false":
	exit(0) #It's better to not rebuild on pr since the secure variables are not shared.

project = TRAVIS_REPO_SLUG.split("/")[1]

package = "%s.unitypackage" % project

url = "https://api.travis-ci.org/repo/%s/requests" % TRAVIS_REPO_SLUG

branch = TRAVIS_BRANCH

headers = {"Content-Type": "application/json",
			"Accept": "application/json",
			"Travis-API-Version": "3",
			"Authorization": API_TOKEN}

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
	GH_TOKEN
except NameError:
	print "Not deploying to Github Releases."
else:
	print "Github token found. Deploying to Github Releases."
	deploy_gh = [
			{
			"provider": "releases",
			"api_key": [
				{
				"secure": GH_TOKEN
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
	print "Post request failed, retrying..."
	r2 = requests.post(url, headers=headers, json=json)
	if r2.status_code != requests.codes.ok:
		raise r2.raise_for_status()
		exit(1)
	else:
		print r2.content
else:
	print response.content



