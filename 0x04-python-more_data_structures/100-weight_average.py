#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum = 0
    weight_total = 0

    for weight in my_list:
        sum += weight[0] * weight[1]
        weight_total += weight[1]

    return sum / weight_total
