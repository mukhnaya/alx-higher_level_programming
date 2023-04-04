#!/usr/bin/python3
'''class square'''


class Square:
    '''body block of square'''

    def __init__(self,size=0):
        self.__size = size

    @property
    def size(self):
        '''gets the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set size of square'''
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''get area'''
        return self.__size * self.__size

    def my_print(self):
        '''print a square of number of size'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#",end="")
                print()
