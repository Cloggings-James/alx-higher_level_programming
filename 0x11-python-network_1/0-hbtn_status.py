#!/usr/bin/python3
"""Script that Fetches a website's status"""

from urllib.request import urlopen, Request

if __name__ == "__main__":
    req = Request("https://example.com")  # Replace with the URL you want to fetch
    with urlopen(req) as resp:
        body = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf8")))

