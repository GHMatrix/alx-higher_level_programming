#!/usr/bin/python3
"""
This script sends a POST request to a given URL
with an email parameter and displays the
body of the response (decoded in utf-8).

Usage: ./2-post_email.py <URL> <email>
"""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    Sends a POST request to the provided URL with
    the email as a parameter and displays
    the body of the response (decoded in utf-8).

    :param url: The URL to send the POST request to.
    :param email: The email parameter to include in the request.
    """
    try:
        data = urllib.parse.urlencode({"email": email}).encode('utf-8')
        with urllib.request.urlopen(url, data=data) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
