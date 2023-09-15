#!/usr/bin/python3
"""Defining a base class"""


class Base:
    """Representing the base class

    Attributes:
    __nb_objects: private class attribute for number of initialized bases
    """

    __nb_objects = 0

    """Initializing class
    Args:
    id: The id of the new base

    """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
