#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest)
of a specified repository by a given owner on GitHub.
"""

import requests
import sys

def list_commits(owner, repo):
    base_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(base_url)
        commits = response.json()

        if response.status_code == 200:
            for commit in commits[:10]:  # Get the first 10 commits
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print("Error: Unable to fetch commits.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    list_commits(owner_name, repository_name)

