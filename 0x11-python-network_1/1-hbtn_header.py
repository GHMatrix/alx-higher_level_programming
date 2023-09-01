#!/usr/bin/python3
"""
This script sends a request to a given URL and
displays the value of the X-Request-Id
variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""

import urllib.request
import sys


def get_x_request_id(url):
    """
    Sends a request to the provided URL and extracts
    and displays the value of the
    X-Request-Id variable from the response header.

    :param url: The URL to send the request to.
    """
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader("X-Request-Id")
            if x_request_id:
                print(x_request_id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
