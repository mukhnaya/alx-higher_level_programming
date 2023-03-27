#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is not None:
        mos = 0
        for pau in my_list:
            mos = mos + 1
        try:
            if x < mos:
                jos = 0
                for jul in range(jos, x):
                    print("{}".format(my_list[jul]), end="")
                print()
        except Exception:
            if x > mos - 1:
                lorio = 0
                for lyn in range(lorio, mos):
                    print("{}".format(my_list[lyn]))

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 4)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
