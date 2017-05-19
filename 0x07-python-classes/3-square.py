#!/usr/bin/python3
""" defines a square by 2-square.py """


class Square:
    """ defining square class """
    def __init__(self, size=0):
        """ initializing self """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ defining area """
        return self.__size ** 2
