#!/usr/bin/python3
""" Function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """ Matrix division function. """

    m1 = "matrix must be a matrix (list of lists) of integers/floats"
    m2 = "Each row of the matrix must have the same size"
    m3 = "div must be a number"
    m4 = "division by zero"

    if type(matrix) is not list:
        raise TypeError(m1)
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError(m1)
    if not all(isinstance(i, int) or isinstance(i, float)
               for x in matrix for i in x):
        raise TypeError(m1)
    if not all(len(x) is len(matrix[0]) for x in matrix):
        raise TypeError(m2)
    if type(div) is not int and type(div) is not float:
        raise TypeError(m3)
    if div is 0:
        raise ZeroDivisionError(m4)
    return [[round(i / div, 2) for i in x] for x in matrix]
