#!/usr/bin/python3
""" Print ASCII alphabet in lowercase with out newline """


for i in range(97, 123):
    if i is 101 or i is 113:
        continue
    print("{:c}".format(i), end="")
