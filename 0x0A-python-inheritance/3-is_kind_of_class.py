#!/usr/bin/python3
'''check if is instance of'''


def is_kind_of_class(obj, a_class):
    '''using is subclass'''
    mos = issubclass(obj, a_class)
    return mos
