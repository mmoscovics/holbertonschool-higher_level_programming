#!/usr/bin/python3
""" Function that reads n lines of a text file and prints to stdout. """


def read_lines(filename="", nb_lines=0):
    """ Reads n lines of a text file and prints to stdout. """

    if filename is '':
        return
    if nb_lines <= 0:
        with open(filename, 'r') as f:
            print(f.read(), end='')
    else:
        with open(filename, 'r') as f:
            for i in range(0, nb_lines):
                print(f.readline(), end='')
