#!/usr/bin/python3
"""
Python script that uses the GitHub API to display your GitHub ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    # Create a Basic Authentication string using your username and token
    auth = (username, token)

    # Make a GET request to the GitHub API
    url = "https://api.github.com/user"
    response = requests.get(url, auth=auth)

    # Check the response status code
    if response.status_code == 200:
        user_data = response.json()
        github_id = user_data.get("id")
        print(github_id)
    else:
        print("None")

