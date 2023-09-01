#!/usr/bin/python3
"""
This script uses GitHub API with Basic Authentication
to display your GitHub user id.
"""

import requests
import sys


def get_github_id(username, password):
    """
    Retrieves your GitHub user id using Basic Authentication
    with a personal access token.

    :param username: Your GitHub username.
    :param password: Your GitHub personal access token.
    :return: Your GitHub user id or None if authentication fails.
    """
    url = 'https://api.github.com/user'
    auth = (username, password)

    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            return user_data['id']
        else:
            return None
    except Exception:
        return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    github_id = get_github_id(username, password)

    if github_id is not None:
        print(github_id)
    else:
        print("None")
