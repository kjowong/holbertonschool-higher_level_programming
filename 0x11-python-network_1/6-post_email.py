#!/usr/bin/python3
"""
    Python script that takes in URL and email, sends POST request to passed
    URL and displays body of the response
"""

from sys import argv
import requests

url = argv[1]
payload = {'email': argv[2]}
req = requests.post(url, data=payload)
print(req.text)
