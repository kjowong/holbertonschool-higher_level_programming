#!/usr/bin/python3
""" defining class Square """


class Square:
    """ initializing self """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ getting size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting size """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ defining area """
        return self.__size ** 2

    def __eq__(self, comp):
        """ defining equal """
        return Square.area(self) == Square.area(comp)

    def __ne__(self, comp):
        """ defining does not """
        return Square.area(self) != Square.area(comp)

    def __gt__(self, comp):
        """ defining more then """
        return Square.area(self) > Square.area(comp)

    def __ge__(self, comp):
        """ defining more equal """
        return Square.area(self) >= Square.area(comp)

    def __lt__(self, comp):
        """ defining less then """
        return Square.area(self) < Square.area(comp)

    def __le__(self, comp):
        """ defining less equal """
        return Square.area(self) <= Square.area(comp)
