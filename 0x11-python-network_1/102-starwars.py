#!/usr/bin/python3
"""
    Python script that takes in a string and sends a search request to
    Star Wars API, lists films associated with the person
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
            for film in person['films']:
                new_req = requests.get(film)
                json_film = new_req.json()
                print("\t{}".format(json_film.get('title')))
