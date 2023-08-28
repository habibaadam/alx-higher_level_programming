#!/usr/bin/python3

def safe_print_integer(value):
    """
A function that prints an integer with "{:d}".format

Args:
   value: the intege to be printed

Return:
    if value is an integer - True
    Otherwise - throw specified type of errors
    """

    try:
        print("{:d}".format(value))
        return (True)
    except(TypeError, ValueError):
        return (False)
