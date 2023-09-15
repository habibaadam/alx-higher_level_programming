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

    @property
    def width(self):
        """Getting the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting and checking the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting and checking the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting and checking the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the class rectangle"""
        return self.__height * self.__width
