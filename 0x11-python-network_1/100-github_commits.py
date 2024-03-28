#!/usr/bin/python3
"""
This module uses the GitHub API to display the 10 most recent commits of a
repository by a user.
"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(url)

    try:
        commits = response.json()
        for commit in commits[:10]:
            print("{}: {}".format(commit['sha'], commit['commit']['author']['name']))
    except ValueError:
        print("Not a valid JSON")
