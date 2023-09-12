#!/usr/bin/python3
"""Defining a function that prints contents of a file"""


def read_file(filename=""):
    """printing contents of file"""
    with open(filename, encoding="utf-8") as h:
        print(h.read(), end="")
