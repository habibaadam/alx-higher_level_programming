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

    def my_print(self):
        """prints in stdout the square with the character #
        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print("")
        else:
            for h in range(0, self.__size):
                [print("#", end="") for m in range(self.__size)]
                print("")
