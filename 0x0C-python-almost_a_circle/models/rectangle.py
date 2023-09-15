#!/usr/bin/python3
"""Defining a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A new rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialzing the class
        Args:
        width: the width of the rectangle
        height: the height of the rectangle
        x: the x coordinate of the rectangle
        y: the y coordinate of the rectangle
        id: represents the identity of the rectangle

        Raises:
        TypeError: if either width or height is not an int
        ValueError: if either width or height is <= 0
        TypeError: If either x or y is not an int
        ValueError: If either x or y is <= 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """
     @property
    def width(self):
        Getting the width
        return self.__width

    @width.setter
    def width(self, value):
        Setting and checking the value of width
        if type(value) is not int:
            raise TypeError("")
    """
