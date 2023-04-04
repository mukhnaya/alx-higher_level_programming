#!/usr/bin/python3
'''creates a square class'''

class Square:
    '''this body is not empty'''
    __size = 0
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
