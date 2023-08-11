#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    lengthoflist = len(my_list) - 1
    if idx < 0 or idx > lengthoflist:
        return my_list.copy()
    else:
        new_my_list = my_list.copy()
        new_my_list[idx] = element
        return new_my_list
