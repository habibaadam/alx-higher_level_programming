#!/usr/bin/python3
"""Defining a class square, inheriting from the class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing the new square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class
        Args:
        size: the size of the new square(width and height)
        width: the width of the square
        height: the height of the square
        x: the x coordinate of the square
        y: the y coordinate of the square
        id: represents the identity of the square

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getting the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value of the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Override string representation of the class
        in the format:
        [Square] (<id>) <x>/<y> - <size>
        """

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height
        )
