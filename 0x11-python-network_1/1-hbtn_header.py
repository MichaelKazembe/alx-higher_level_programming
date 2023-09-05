#!/usr/bin/python3
import urllib.request
import sys

"""
This script takes in a URL as a command-line argument
sends a request to the URL, and displays the value of
the X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
