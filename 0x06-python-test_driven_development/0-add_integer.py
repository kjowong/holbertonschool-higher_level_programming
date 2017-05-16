#!/usr/bin/python3
""" add_integer file function"""


def add_integer(a, b):
    """ add_integer function """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
