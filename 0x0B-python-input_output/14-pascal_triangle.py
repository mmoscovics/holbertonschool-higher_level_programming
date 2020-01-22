#!/usr/bin/python3
""" Function that returns a list of lists of integers
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """ Returns representation of Pascal's triangle of n. """

    tri = []
    for pos in range(1, n + 1):
        tri.append([1] * pos)
    for y in range(2, n):
        row = tri[y]
        prev_row = tri[y - 1]
        for x in range(1, len(row) - 1):
            row[x] = prev_row[x - 1] + prev_row[x]
    return tri
