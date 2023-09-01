#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
The letter is sent in the variable q.
If no argument is given, q is set to an empty string.
It displays the id and name from the JSON response if
the response is properly formatted and not empty.
Otherwise, it displays appropriate error messages.

Usage: ./8-json_api.py <letter>
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request to search_user API and displays
    the id and name from the response if valid.

    :param letter: The letter to search for.
    """
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        user_data = response.json()

        if user_data:
            print("[{}] {}".format(user_data['id'], user_data['name']))
        else:
            print("No result")

    except requests.exceptions.HTTPError as e:
        print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        search_user("")
    else:
        letter = sys.argv[1]
        search_user(letter)
