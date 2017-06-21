#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for key in my_dict:
        new_value = my_dict[key] * 2
        new_dict[key] = new_value
    return new_dict
