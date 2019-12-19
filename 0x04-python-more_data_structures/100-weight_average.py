#!/usr/bin/python3
""" Returns weighted average of all integer tuple """


def weight_average(my_list=[]):
    """ Returns weighted average """

    if not my_list:
        return 0
    total = 0
    weight = 0
    for i in my_list:
        total += i[0] * i[1]
        weight += i[1]
    return total / weight
