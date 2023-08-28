#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """A function that prints the first x elements of a list
       Other type of value in the list must be skipped (in silence).

Args:
  my_list: contains the list of elements
  x: first number of elements(int) to be printed out from my_list
Return:
  number of integers in the list
   """
    counter = 0
    for h in range(0, x):
        try:
            print("{:d}".format(my_list[h]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (counter)
