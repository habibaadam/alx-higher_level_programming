#!/usr/bin/python3
"""Defining class BaseGeometry"""


class BaseGeometry:
    """Initializing class"""
    def area(self):
        """raising an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
