#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command line argument
    email = sys.argv[2]  # Get the email from the command line argument

    # Create a dictionary with the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')  # Create a POST request object

    with urllib.request.urlopen(req) as response:
        # Read and decode the response body
        response_body = response.read().decode('utf-8')
        print("Your email is: {}".format(response_body))

