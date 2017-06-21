#!/usr/bin/python3
""" size validation function """


class Square:
    """ defining square class """
    def __init__(self, size=0):
        """ initializing set """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
