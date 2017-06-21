#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ defining inherit from """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
