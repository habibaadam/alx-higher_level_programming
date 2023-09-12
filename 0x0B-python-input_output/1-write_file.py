#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """writes a string to the existing file"""
    with open(filename, "w", encoding="utf-8") as h:
        return h.write(text)
