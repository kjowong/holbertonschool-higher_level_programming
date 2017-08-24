#!/usr/bin/python3
"""
    Python script that takes in your Github credentials and uses Github API to
    display your id
"""

from sys import argv
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    resp = requests.get('https://api.github.com/user',
                        auth=HTTPBasicAuth(username, password))
    json = resp.json()
    print(json.get('id'))
