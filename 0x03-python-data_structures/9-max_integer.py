#!/usr/bin/python3

def max_integer(my_list=[]):
    lengthofmylist = len(my_list) - 1
    if lengthofmylist == 0:
        return None

    largest = my_list[0]
    for h in range(lengthofmylist):
        if my_list[h] > largest:
            largest = my_list[h]
    return largest
