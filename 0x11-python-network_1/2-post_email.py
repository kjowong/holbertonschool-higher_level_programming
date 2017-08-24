#!/usr/bin/python3
"""
    Python script that takes in a URL and email - sends a POST to
    passed URL, displays body of response
"""
from sys import argv
import urllib.parse
import urllib.request


url = argv[1]
values = {'email': argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    html = response.read()
print(html.decode('utf8'))
