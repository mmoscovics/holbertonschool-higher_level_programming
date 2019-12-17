#!/usr/bin/python3
""" Finds all multiples of 2 in a list """


def divisible_by_2(my_list=[]):
    """ Returns true or false """

    tf = []

    for i in my_list:
        if i % 2 is 0:
            tf.append(True)
        else:
            tf.append(False)
    return tf
