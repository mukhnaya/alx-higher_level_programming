#!/usr/bin/python3
'''class square to for getters and setters'''


class Square:
    '''body of the Square class'''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        '''returns size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the value of size'''
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''gets area'''
        return self.__size * self.__size
