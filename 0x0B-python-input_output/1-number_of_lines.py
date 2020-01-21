#!/usr/bin/python3
""" Function that returns the number of lines of a text file. """


def number_of_lines(filename=""):
    """ Returns the number of lines of a text file. """

    line_count = 0

    if filename is '':
        return
    with open(filename, 'r') as f:
        for line in f:
            line_count += 1
    return line_count
