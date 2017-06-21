#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ defining load from json file """
    with open(filename, "r") as f:
        return json.load(f)
