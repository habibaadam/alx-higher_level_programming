#!/usr/bin/python3
def element_at(my_list, idx):
    """
    If idx is out of range (> of number of element in my_list),
    the function should return None
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
