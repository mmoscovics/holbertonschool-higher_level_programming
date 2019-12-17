#!/usr/bin/python3
""" Returns biggest int of a list """


def max_integer(my_list=[]):
    """ Returns biggest int """

    if my_list is None or len(my_list) is 0:
        return None
    max_int = my_list[0]
    for i in my_list:
        if max_int < i:
            max_int = i
    return max_int
