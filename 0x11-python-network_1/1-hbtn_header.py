#!/usr/bin/python3
"""
Python script that Takes in a URL,
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            header = resp.headers.get('X-Request-Id')
            print(header)
    except IndexError:
        print("Usage: python script.py <URL>")
    except urllib.error.URLError as e:
        print(f"Error: {e}")

