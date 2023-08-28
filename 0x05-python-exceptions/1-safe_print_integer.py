#!/usr/bin/python3

"""
A function that prints an integer with "{:d}".format()
value can be any type (integer, string, etc.)

Args:
    value: integer to be printed out.
Return:
  If a specific error occurs,in case of the value not being an integer - False
  If not - True
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except(TypeError, ValueError):
        return False
