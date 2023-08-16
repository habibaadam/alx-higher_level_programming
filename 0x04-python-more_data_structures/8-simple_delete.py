#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """delete key in a_dictionary only if it exists"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
