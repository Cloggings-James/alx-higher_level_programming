#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command line argument

    req = urllib.request.Request(url)  # Create a request object
    with urllib.request.urlopen(req) as response:
        # Check if 'X-Request-Id' exists in the headers
        if 'X-Request-Id' in response.info():
            x_request_id = response.info()['X-Request-Id']
            print(x_request_id)

