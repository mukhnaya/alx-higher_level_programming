#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pau = 0
    for mos in range(x):
        try:
            print("{:d}".format(my_list[mos]), end="")
            pau = pau + 1
        except (TypeError, ValueError):
            pass
    print()
    return pau
