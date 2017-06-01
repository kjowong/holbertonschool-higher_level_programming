#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defining class Square """
    def __init__(self, size):
        """ initializing self """
        Rectangle.__init__(self, size, size)
