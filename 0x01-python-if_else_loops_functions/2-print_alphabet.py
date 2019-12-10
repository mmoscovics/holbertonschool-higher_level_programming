#!/usr/bin/python3
""" Print ASCII alphabet in lowercase with out newline """


for i in range(97, 123):
    print("{:c}".format(i), end="")
