#!/usr/bin/python3
"""
This module contains a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers or floats and
    raises Typerror if a or b is not an int/float

    Args:
    a: first number
    b: second number

    Return: the addition of the two numbers.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
