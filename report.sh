COMMENT='{"body":"Checking Commenting Capabilities"}'
curl -H "Authorization: token $GITHUB_TOKEN" -X POST -d ${COMMENT} "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
