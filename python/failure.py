import requests
import json
import sys
import datetime
TRAVIS_BUILD_NUMBER = sys.argv[1]
TRAVIS_BUILD_WEB_URL = sys.argv[2]

payload_json = {
    "embeds": [{
        "title": "WormJam CI Report",
        "color": 10027008,
        "description": "Travis CI Build",
        "fields":[
            {
                "name": "Build Number",
                "value":str(TRAVIS_BUILD_NUMBER)
            },
            {
                "name":"Build logs",
                "value":"Logs can be found [here]("+TRAVIS_BUILD_WEB_URL+")"
            }
        ],
        "timestamp": str(datetime.datetime.now().isoformat())
    }]
}