#!/usr/bin/python3
"""
This script fetches data from a URL using the requests
package and displays information about the response.

Usage: ./4-hbtn_status.py | cat -e
"""

import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("    - type:", type(content))
    print("    - content:", content)
except Exception as e:
    print("An error occurred:", e)
