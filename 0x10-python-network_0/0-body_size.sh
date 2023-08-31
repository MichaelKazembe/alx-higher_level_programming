#!/bin/bash
# displays the size of the body of the response(Content-length)

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
