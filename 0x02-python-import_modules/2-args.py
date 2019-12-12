#!/usr/bin/python3
""" Prints number of and the list of arguments """


from sys import argv


if __name__ == "__main__":
    if len(argv) is 1:
        print("0 arguments.")
    elif len(argv) is 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv)-1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
