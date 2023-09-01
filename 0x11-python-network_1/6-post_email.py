#!/usr/bin/python3
"""
This script sends a POST request to a given URL with
an email parameter and displays the body of the response.

Usage: ./6-post_email.py <URL> <email>
"""

import requests
import sys


def post_email(url, email):
    """
    Sends a POST request to the provided URL with
    the email as a parameter and displays
    the body of the response.

    :param url: The URL to send the POST request to.
    :param email: The email parameter to include in the request.
    """
    try:
        data = {"email": email}
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors

        print(f"Your email is: {email}")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
