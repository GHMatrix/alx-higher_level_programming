#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest)
of a GitHub repository by a specified owner.
"""

import requests
import sys


def list_commits(repo_name, owner_name):
    """
    Lists 10 commits (from the most recent to oldest)
    of a GitHub repository by a specified owner.

    :param repo_name: The name of the repository.
    :param owner_name: The name of the repository owner.
    """
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')

    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
