#!/usr/bin/python3
"""Script that Fetches https://intranet.hbtn.io/status"""

Fetches the status of a URL using the urllib package and displays response information.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content.decode('utf-8')))

