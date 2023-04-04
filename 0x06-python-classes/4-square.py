#!/usr/bin/python3
'''class square to for getters and setters'''


class Square:
    '''body of the Square class'''

    def __init(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def size(self, value):
        self.size = value
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
