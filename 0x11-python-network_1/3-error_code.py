#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request and
    displays the body of the response
"""
from sys import argv
import urllib.request


req = urllib.request.Request(argv[1])
try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
