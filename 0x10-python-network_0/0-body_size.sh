#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Send a GET request and retrieve the response headers
response_headers=$(curl -sI "$url")

# Extract the Content-Length header value from the response headers
content_length=$(echo "$response_headers" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

echo "$content_length"
