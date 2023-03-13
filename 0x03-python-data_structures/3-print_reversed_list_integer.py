#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
    '''pau = len(my_list) - 1
    mos = 0
    if pau == 0:

    while pau >= mos:
        print("{:d}".format(my_list[pau]))
        pau -= 1
    '''
