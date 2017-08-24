#!/usr/bin/python3
"""
    Python script that takes in a URL, sends request and displays value
    of X-Request-Id in header of the response
"""


import sys
import urllib.request
req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    html = response.getheader('X-Request-Id')
print(html)
