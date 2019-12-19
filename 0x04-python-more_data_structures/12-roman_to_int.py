#!/usr/bin/python3
""" Converts Roman numerals to integers """


def roman_to_int(roman_string):
    """ Converts Roman numerals to ints """

    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10,"L": 50, "C": 100,
                  "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string)):
        val = roman_dict[roman_string[i]]
        if i < len(roman_string) - 1:
            next_val = roman_dict[roman_string[i + 1]]
        if i is len(roman_string) - 1:
            total += val
        elif next_val > val:
            total += next_val - val
        else:
            total += val
    return total
