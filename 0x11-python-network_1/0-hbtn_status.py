#!/usr/bin/python3
"""
Fetches the status of a URL using the urllib package and displays response information.
"""

from urllib.request import urlopen, Request

if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))

