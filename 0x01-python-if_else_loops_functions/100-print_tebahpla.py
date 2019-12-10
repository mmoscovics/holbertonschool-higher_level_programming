#!/usr/bin/python3
""" Prints ASCII alphebet in reverse with alternate caps """


for i in range(122, 96, -1):
    if i % 2 is 1:
        i = i - 32
    print("{:c}".format(i), end="")
