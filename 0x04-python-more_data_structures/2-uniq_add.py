#!/usr/bin/python3

def uniq_add(my_list=[]):
    """using a set to filter out duplicates"""
    uniq = set(my_list)
    addeduniq = 0

    for h in uniq:
        addeduniq += h

    return addeduniq
