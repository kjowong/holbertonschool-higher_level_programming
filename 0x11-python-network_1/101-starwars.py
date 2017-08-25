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
        print("Number of result: {}".format(json.get('count')))
        result = json.get('results')
        for person in result:
            print(person.get('name'))
        next_page = json.get('next')
        if next_page:
            next_api_call = requests.get(next_page)
            next_json = next_api_call.json()
            next_result = next_json.get('results')
            for person in next_result:
                print(person.get('name'))
