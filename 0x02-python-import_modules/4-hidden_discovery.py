#!/usr/bin/python3
""" Prints all names defined by a compiled module """


import hidden_4


if __name__ == "__main__":
    arr = dir(hidden_4)
    for i in arr:
        if i[0] is not "_":
            print(i)
