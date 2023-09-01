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
    response.raise_for_status()  # Raise an exception for HTTP errors
    content = response.text

    print("Body response:")
    print("    - type:", type(content))
    print("    - content:", content)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print("An unexpected error occurred:", e)
