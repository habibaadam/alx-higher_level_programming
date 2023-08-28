#!usr/bin/python3

"""
A function that prints a list of integers

Args:
  my_list: contains list of numbers
  x: maximum number of elements to print out.
Return:
  number of elements printed out if a specified error does not occur

"""


def safe_print_list(my_list=[], x=0):
    counter = 0
    for h in range(x):
        try:
            print("{}".format(my_list[h]), end="")
            counter += 1
        except IndexError:
            break
    print("")
    return counter
