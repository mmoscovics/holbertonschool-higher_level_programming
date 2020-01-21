#!/usr/bin/python3
""" Function that reads a text file and prints it to stdout. """


def read_file(filename=""):
    """ Reads a text file and prints to stdout. """

    with open(filename, 'r') as f:
        print(f.read()[:-1])
