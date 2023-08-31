#!/bin/bash
# displays the size of the body of the response(Content-length)

url="$1"
curl -sI "$url" | grep -i Content-Length | awk '{print $2}'
