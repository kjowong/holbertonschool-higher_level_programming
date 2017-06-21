#!/usr/bin/python3
""" defines a square based on 4-square.py """


class Square:
    """ defining square class """
    def __init__(self, size=0):
        """ initializing self """
        self.__size = size

    @property
    def size(self):
        """ getting size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ defining area """
        return self.__size ** 2

    def my_print(self):
        """ defining print """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
