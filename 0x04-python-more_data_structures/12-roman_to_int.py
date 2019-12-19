#!/usr/bin/python3
""" Converts Roman numerals to integers """


def roman_to_int(roman_string):
    """ Converts Roman numerals to ints """

    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
    total = 0
    i = 0
    while i < len(roman_string):
        val = roman_dict[roman_string[i]]
        if i < len(roman_string) - 1:
            next_val = roman_dict[roman_string[i + 1]]
            if val >= next_val:
                total += val
                i += 1
            else:
                total += next_val - val
                i += 2
        else:
            total += val
            i += 1
    return total
