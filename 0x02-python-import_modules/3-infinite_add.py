#!/usr/bin/python3
""" Prints result of addition of all arguments """


from sys import argv


if __name__ == "__main__":
    total = 0

    if len(argv) is 1:
        print(total)
    else:
        for i in range(1, len(argv)):
            total += int(argv[i])
        print(total)
