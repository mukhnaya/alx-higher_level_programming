#!/usr/bin/python3
'''return true if is instance of class'''


def is_same_class(obj, a_class):
    '''using isinstance function'''
    mos = isinstance(obj, a_class)
    return mos

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
