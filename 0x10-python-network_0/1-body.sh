#!/bin/bash
# Bash script  that takes in a URL, sends a GET request to the URL, and displays the body of the response.
# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Send a GET request and store the response in a variable
response=$(curl -s -w "%{http_code}" -L "$url")

# Extract the status code from the response
status_code="${response: -3}"

# Check if the status code is 200
if [ "$status_code" = "200" ]; then
    # Remove the last 3 characters (status code) from the response
    body="${response::-3}"
    echo "$body"
else
    echo "Error: Status code $status_code"
fi
