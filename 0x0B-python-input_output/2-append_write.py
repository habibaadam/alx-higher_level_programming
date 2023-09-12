#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """appending string to file"""
    with open(filename, "a", encoding="utf-8") as ha:
        return ha.write(text)
