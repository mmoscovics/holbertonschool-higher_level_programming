#!/usr/bin/python3
""" Print all integers of a list in reverse order """


def print_reversed_list_integer(my_list=[]):
    """ Prints integers of list in reverse """

    for i in range(len(my_list), 0, -1):
        print("{:d}".format(i))
