#!/usr/bin/python3
'''check if inherits from a class'''


def inherits_from(obj, a_class):
    '''use sub class'''
    if type(obj) != a_class:
        mos = issubclass(type(obj), a_class)
        return mos
    else:
        return False
