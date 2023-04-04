#!/usr/bin/python3
'''declaration of class Square'''


class Square:
    '''body of the class square'''
    def __init__(self, size=0):
        '''init method to initialize size of square'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''get method to return area of square'''
        return self.__size * self.__size
