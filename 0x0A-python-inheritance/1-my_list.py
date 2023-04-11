#!/usr/bin/python3
'''to inherit from list'''


class MyList(list):
    '''print a list'''
    def print_sorted(self):
        print(sorted(self))
