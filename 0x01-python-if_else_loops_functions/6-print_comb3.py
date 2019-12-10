#!/usr/bin/python3
""" Prints all possible different combinations of two digits """


for i in range(10):
    for j in range(10):
        if j > i:
            if i < 8:
                print("{}{}".format(i, j), end=", ")
            else:
                print("{}{}".format(i, j))
