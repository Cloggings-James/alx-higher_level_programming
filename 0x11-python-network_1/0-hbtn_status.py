python
import urllib.request

def fetch_status():
    try:
        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except urllib.error.URLError as e:
        print("Error: {}".format(e.reason))

if __name__ == "__main__":
    fetch_status()
