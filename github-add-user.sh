#!/bin/bash
# Collaborator list, add, remove from a repository
# (c) 2015 miraculixx
# Author: github.com/miraculixx
# MIT License, see below

function help {
  echo "Add collaborators to one or more repositories on github"
  echo ""
  echo "Syntax:   $0 -H GITHUB_OAUTH_TOKEN [-l] [-D] -r repo1,repo2 <collaborator id1>,<collaborator id2>"
  echo ""
  echo "          -H    OAUTH toekn"
  echo "          -l    list collaborators"
  echo "          -r    repositories, list as owner/repo[,owner/repo,...]"
  echo "          -D    remove"
  echo "          id    the collaborator id to add or remove"
}

while getopts "h?H:r:D:l?" opt; do
    case $opt in
      h|\?)
         help
         exit 0
         ;;
      H)
         GITHUB_OAUTH_TOKEN=$OPTARG
         ;;
      D)
         METHOD=DELETE
         ;;
      r)
         REPOS=$OPTARG
         ;;
      l)
         LIST=yes
         ;;
    esac
done

shift $((OPTIND-1))

COL_USER=$1

if [[ -z "$GITHUB_OAUTH_TOKEN" ]]; then
   echo Enter your github api oauth token
   read GITHUB_OAUTH_TOKEN
fi

if [[ -z "$REPOS" ]]; then
   echo Enter the repositories as user/repo. Multiple repos comma separated.
   read REPOS
fi

if [[ -z "$COL_USER" ]]; then
   LIST=yes
fi

if [[ -z "$METHOD" ]] && [[ ! -z "$COL_USER" ]]; then
   echo "[WARN] Assuming you want to add user $COL_USER. Use the -D option to delete"
   METHOD=PUT
fi

repos=(${REPOS//,/ })
collaborators=(${COL_USER//,/ })

if [[ ! -z "$COL_USER" ]]; then
  for repo in "${repos[@]}"; do
    for collaborator in "${collaborators[@]}"; do
      echo "[INFO] $METHOD $collaborator to $repo"
      curl -i -H "Authorization: token $GITHUB_OAUTH_TOKEN" -X $METHOD -d '' "https://api.github.com/repos/$repo/collaborators/$collaborator" 2>&1 | grep message || echo "OK, done."
    done
  done
fi


if [[ ! -z "$LIST" ]]; then
   for repo in "${repos[@]}"; do
     echo "[INFO] Current list of collaborators in $repo:"
     curl -i -H "Authorization: token $GITHUB_OAUTH_TOKEN" -X GET -d '' "https://api.github.com/repos/$repo/collaborators" 2>&1 | grep login
   done
fi

exit 0

: <<< 'EOF'
The MIT License (MIT)

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
EOF