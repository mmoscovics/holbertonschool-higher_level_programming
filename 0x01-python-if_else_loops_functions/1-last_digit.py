#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ld = abs(number) % 10 * -1
else:
    ld = number % 10
if ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, ld))
if ld is 0:
    print("Last digit of {} is {} and is 0".format(number, ld))
if ld is not 0 and ld < 6:
    print("Last digit of {} is {} and is less than 6 \
    and not 0".format(number, ld))
