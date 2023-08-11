#!/usr/bin/python3
def element_at(my_list, idx):
    lengthoflist = len(my_list) - 1
    """
    If idx is out of range (> of number of element in my_list),
    the function should return None
    """
    if idx < 0 or idx > lengthoflist:
        return None
    else:
        return(my_list[idx])
