#!/usr/bin/python3
""" Prints last digit of a number """


def print_last_digit(number):
    """ Prints last digit of a number """

    ld = abs(number) % 10
    print(ld, end="")
    return ld
