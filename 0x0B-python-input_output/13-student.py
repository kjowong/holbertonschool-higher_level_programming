#!/usr/bin/python3
""" student to disk and reload """


class Student:
    """ defining student class """
    def __init__(self, first_name, last_name, age):
        """ initializing self """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ defining to json """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict

    def reload_from_json(self, json):
        """ defining reload to json """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
