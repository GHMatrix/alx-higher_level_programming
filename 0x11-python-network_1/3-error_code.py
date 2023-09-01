#!/usr/bin/python3
"""
This script sends a request to a given URL and
displays the body of the response (decoded in utf-8).
It also handles HTTP errors and prints the
HTTP status code in case of an error.

Usage: ./3-error_code.py <URL>
"""

import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """
    Sends a request to the provided URL and displays the body of the response
    (decoded in utf-8). Handles HTTP errors and prints the
    HTTP status code in case of an error.

    :param url: The URL to send the request to.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_content(url)
