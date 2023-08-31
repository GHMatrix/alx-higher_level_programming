#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
[ $# -ne 1 ] && echo "Usage: $0 <URL>" && exit 1; curl -sI "$1" | grep -i "Allow" | cut -d':' -f2- | tr -d ' ' | tr ',' ', '
