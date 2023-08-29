#!/usr/bin/python3
"""Defining a class representing a square"""


class Square:
    """Initializing the square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getting current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Checking value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square"""
        return self.__size * self.__size
    
    def __equal__(self, other):
        return self.area() == other.area()

    def __notequal__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lessthan__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __lessthanE__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __greaterthan__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __greaterthanE__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
