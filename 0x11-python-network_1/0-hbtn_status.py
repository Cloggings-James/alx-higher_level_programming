# Import the urllib.request module
import urllib.request

# Define the URL to fetch
url = "https://alx-intranet.hbtn.io/status"

# Open the URL and store the response object
with urllib.request.urlopen(url) as response:
    # Read the data from the response object as bytes
    data = response.read()
    # Decode the data as UTF-8 string
    data_str = data.decode("utf-8")

    # Print the body of the response
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data_str))

