#!/usr/bin/python3
""" student to Json with filter"""


class Student:
    """ defining class Student """
    def __init__(self, first_name, last_name, age):
        """ initializing self """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ defining to_json """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict
        return self.__dict__
