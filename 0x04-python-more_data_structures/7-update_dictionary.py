#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    for key_t in list(my_dict):
        if key_t != key:
            my_dict[key] = value
        if key_t == key:
            my_dict[key_t] = value
    return my_dict
