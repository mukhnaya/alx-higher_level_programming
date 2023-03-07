#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = int(repr(number)[-1])
las_dig = "Last digit of"
great_5 = "and is greater than 5"
les_6 = "and is less than 6 and not 0"
is_zero = "and is 0"
if (last_dig > 5):
    print("{0} {1} is {2} and {3}".format(las_dig, number, last_dig, great_5))
elif (last_dig < 6 and last_dig != 0):
    print("{0} {1} is {2} and {3}".format(las_dig, number, last_dig, les_6))
else:
    print("{0} {1} is {2} and and {3}".format(las_dig, number, last_dig, is_zero))
