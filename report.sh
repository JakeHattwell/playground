COMMENT="Hi There"
curl -H "Authorization: token $GITHUB_TOKEN" -X POST -d "{\"body\":\"Checking Commenting Capabilities\"}" "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
