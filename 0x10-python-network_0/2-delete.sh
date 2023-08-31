#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
[ $# -ne 1 ] && echo "Usage: $0 <URL>" && exit 1; curl -sX DELETE "$1" -L
