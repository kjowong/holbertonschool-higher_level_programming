#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ defining class Square """
    def __init__(self, size):
        """ initializing self """
        Rectangle.__init__(self, size, size)
        self.__width = size
        self.__height = size

    def __str__(self):
        """ defining str """
        str1 = "[Square] {}/{}".format(self.__width, self.__height)
        return str1
