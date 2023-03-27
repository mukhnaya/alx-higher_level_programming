#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is not None:
        mos = 0
        for pau in my_list:
            mos = mos + 1
        try:
                jos = 0
                for jul in range(jos, x):
                    print("{:d}".format(my_list[jul]), end="")
        except IndexError:
            pass
        print()
    return mos
