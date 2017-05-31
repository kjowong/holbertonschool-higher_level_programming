#!/usr/bin/python3
class BaseGeometry:
    """ defining class BaseGeometry """
    def area(self):
        """ defining area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ defining integer_validator """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
