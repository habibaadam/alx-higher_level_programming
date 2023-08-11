#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    lengthoflist = len(my_list) - 1
    """
    If idx is negative, the function should not modify anything,
    and returns the original list
    If idx is out of range (> of number of element in my_list),
    the function should not modify anything, and returns the original list
    """
    if idx < 0 or idx > lengthoflist:
        return my_list
    else:
        my_list[idx] = element
        return my_list
