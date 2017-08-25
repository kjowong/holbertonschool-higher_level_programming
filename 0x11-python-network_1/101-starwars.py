#!/usr/bin/python3
"""
    Python script that takes in a string and sends a search request to
    Star Wars API
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = requests.get('https://swapi.co/api/people/?search={}'
                       .format(argv[1]))
    if url.headers['Content-type'] == 'application/json':
        json = url.json()
        print("Number of results: {}".format(json.get('count')))
        result = json.get('results')
        i = 0
        while (i <= len(json['results'])):
            if json.get('next') is not None and i == len(json['results']):
                json = requests.get(json.get('next')).json()
                i = 0
            try:
                print(json.get('results')[i].get('name'))
            except:
                pass
            i += 1
