#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        dividing = a / b
    except (TypeError, ZeroDivisionError):
        dividing = None
    finally:
        print("Inside result: {}".format(dividing))
    return dividing
