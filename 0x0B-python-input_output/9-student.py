#!/usr/bin/python3
"""Defining a class student"""


class Student:
    """Initializing the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method returning dict representation of Student"""
        return self.__dict__
