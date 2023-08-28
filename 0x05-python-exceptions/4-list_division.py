#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for h in range(0, list_length):
        try:
            dividing = my_list_1[h] / my_list_2[h]
        except TypeError:
            print("wrong type")
            dividing = 0
        except ZeroDivisionError:
            print("division by 0")
            dividing = 0
        except IndexError:
            print("out of range")
            dividing = 0
        finally:
            new_list.append(dividing)
    return new_list
