#!/usr/bin/python3
"""
    Python script that takes in a URL, sends request and displays body
    of the response
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = requests.get(argv[1])
    if url.status_code >= 400:
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)
