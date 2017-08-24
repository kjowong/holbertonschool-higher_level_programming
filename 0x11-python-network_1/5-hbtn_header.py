#!/usr/bin/python3
"""
    Python script that takes in a URL, sends request, and displays
    the value of the variable X-Request-Id
"""

from sys import argv
import requests

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers['X-Request-Id'])
