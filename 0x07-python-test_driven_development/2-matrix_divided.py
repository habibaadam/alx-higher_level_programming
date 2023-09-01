#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
Function that divides all elements of a matrix.

    Args:
    matrix: a matrix (list of lists) of integers/floats
    div: a number (integer or float) dividing the matrix

    Returns:
    New matrix containing results of division

    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    mssg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(mssg)

    el_len = 0
    mssg_2 = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(mssg_2)
        """matrix must be of the same size, otherwise raise a TypeError"""
        if el_len != 0 and len(elements) != el_len:
            raise TypeError(mssg_2)

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(mssg_2)

        el_len = len(elements)

    h = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return h
