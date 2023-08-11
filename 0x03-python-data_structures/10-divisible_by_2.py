#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiplesof2 = []
    for h in range(len(my_list)):
        if my_list[h] % 2 == 0:
            multiplesof2.append(True)
        else:
            multiplesof2.append(False)

    return multiplesof2
