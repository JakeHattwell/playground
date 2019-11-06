import json
import sys
import os
import requests

API_KEY = sys.argv[1]
REPO_SLUG = sys.argv[2]
PULL_REQUEST = sys.argv[3]

API_ENDPOINT = "https://api.github.com/repos/%s/issues/%s/comments"%(REPO_SLUG,PULL_REQUEST)

print(API_KEY)
print(REPO_SLUG)
print(PULL_REQUEST)
print(API_ENDPOINT)

headers = {'Authorization':'token '+API_KEY}

for i in os.listdir():
    if "travis_wait" in i:
        with open(i) as f:
            data = {"body":f.read()}

        json_data = json.dumps(data)

        comment = requests.post(API_ENDPOINT,headers=headers,data=json_data)