#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices

    Args:
    m_a: first matrix
    m_b: second matrix

    Returns:
    A product of the two matrices

    Raises:
    TypeError: if either m_a or m_b is not a list
    TypeError: if either m_a or m_b is not a list of lists
    ValueError: if either m_a or m_b is empty
    TypeEroor: if one element of the list of lists is not an int or float
    TypeError: if the rows arent of equal size
    ValueError: if either m_a or m_b cannnot be multiplied

    """

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    for contents in m_a:
        if not isinstance(contents, list):
            raise TypeError("m_a must be a list of lists")

    for contents in m_b:
        if not isinstance(contents, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_a) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for contents in lists:
            if not type(contents) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for contents in lists:
            if not type(contents) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    row_ma = 0

    for contents in m_a:
        if row_ma != 0 and row_ma != len(contents):
            raise TypeError("each row of m_a must be of the same size")
        row_ma = len(contents)

    row_mb = 0

    for contents in m_b:
        if row_mb != 0 and row_mb != len(contents):
            raise TypeError("each row of m_b must be of the same size")
        row_mb = len(contents)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """Matrix Multiplicatiom"""

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            product = sum(m_a[i][h] * m_b[h][j] for h in range(len(m_b)))
            row.append(product)
        result.append(row)
    return result
