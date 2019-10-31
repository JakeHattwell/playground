setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout -b devel
  git add . *.html
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin-devel https://${GH_TOKEN}@github.com/JakeHattwell/wormjam-ci-test.git > /dev/null 2>&1
  git push --quiet --set-upstream origin-devel devel 
}

setup_git
commit_website_files
upload_files