#!/usr/bin/python3
""" FIZZBUZZ numbers from 1 to 100 """


def fizzbuzz():
    """ Prints numbers from 1 to 100 with Fizzbuzz """

    for i in range(1, 101):
        if i % 15 is 0:
            print("FizzBuzz", end=" ")
        elif i % 5 is 0:
            print("Buzz", end=" ")
        elif i % 3 is 0:
            print("Fizz", end=" ")
        else:
            print(i, end=" ")
