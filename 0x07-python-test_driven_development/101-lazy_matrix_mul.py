#!/usr/bin/python3
"""
A function that multiplies 2 matrices by using the module NumPy

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function multiplying 2 matrices

    Args:
    m_a: first matrix
    m_b: second matrix

    Returns:
    Product of multiplication

    """

    return np.matmul(m_a, m_b)
