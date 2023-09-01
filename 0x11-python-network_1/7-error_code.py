#!/usr/bin/python3
"""
This script sends a request to a given URL,
displays the body of the response, and prints
the error code if the HTTP status code is greater than or equal to 400.

Usage: ./7-error_code.py <URL>
"""

import requests
import sys


def fetch_url_content(url):
    """
    Sends a request to the provided URL, displays the body of the response, and
    prints the error code if the HTTP status code
    is greater than or equal to 400.

    :param url: The URL to send the request to.
    """
    try:
        response = requests.get(url)
        content = response.text

        print(content)

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_content(url)
