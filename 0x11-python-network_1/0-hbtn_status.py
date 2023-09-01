#!/usr/bin/python3
"""
This script fetches data from a URL using urllib and
provides information about the response.

Usage: ./0-hbtn_status.py | cat -e
"""

import urllib.request


def fetch_and_display_status(url):
    """
    Fetches content from the given URL and displays
    information about the response.

    :param url: The URL to fetch data from.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            utf8_content = content.decode('utf-8')

            print("Body response:")
            print("    - type:", type(content))
            print("    - content:", content)
            print("    - utf8 content:", utf8_content)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_and_display_status(url)
