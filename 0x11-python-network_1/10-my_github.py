#!/usr/bin/python3
"""
This module uses the GitHub API to display a user's id.
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))

    try:
        json_response = response.json()
        print(json_response.get('id'))
    except ValueError:
        print("Not a valid JSON")
