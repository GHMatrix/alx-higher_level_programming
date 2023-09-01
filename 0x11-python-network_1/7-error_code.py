#!/usr/bin/python3
"""
This script sends a request to a given URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints an error code followed by the value of the HTTP status code.
"""

import requests
import sys


def fetch_url_content(url):
    """
    Sends a request to the provided URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400,
    it prints an error code followed by the value of the HTTP status code.

    :param url: The URL to send the request to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        print(content)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_content(url)
