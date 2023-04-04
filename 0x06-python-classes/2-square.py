#!/usr/bin/python3
'''class declaration'''


class Square:
    '''this body is not empty'''

    def __init__(self, size=0):
        '''initialization of size'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
