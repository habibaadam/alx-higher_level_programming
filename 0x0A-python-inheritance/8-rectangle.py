#!/sur/bin/python3
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


class Rectangle(BaseGeometry):
    """a class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
