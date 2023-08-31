#!/bin/bash
# takes in a URL, sends a GET request to the URL
# displays the body of the response

url="$1"
curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}'
