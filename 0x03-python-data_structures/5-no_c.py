#!/usr/bin/python3

def no_c(my_string):
    new_string = [h for h in my_string if h != 'c' and h != 'C']
    return ("".join(new_string))
