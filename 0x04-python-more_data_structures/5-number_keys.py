#!/usr/bin/python3
def number_keys(my_dict):
    counter = 0
    for key in my_dict:
        if key in my_dict:
            counter += 1
    return counter
