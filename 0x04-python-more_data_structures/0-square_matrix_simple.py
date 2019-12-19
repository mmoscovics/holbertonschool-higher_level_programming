#!/usr/bin/python3
""" Computes square value of all integers of a matrix """


def square_matrix_simple(matrix=[]):
    """ Computes square value of matrix """

    return [[element ** 2 for element in row] for row in matrix]
