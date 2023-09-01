#!/usr/bin/python3
"""
This script sends a request to a given URL and displays
the value of the "X-Request-Id" variable
found in the response header.

Usage: ./5-hbtn_header.py <URL>
"""

import requests
import sys


def get_x_request_id(url):
    """
    Sends a request to the provided URL and displays
    the value of the "X-Request-Id" variable
    found in the response header.

    :param url: The URL to send the request to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
