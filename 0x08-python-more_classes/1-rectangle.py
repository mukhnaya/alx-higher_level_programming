#!/usr/bin/python3
'''Rectangle class declaration'''


class Rectangle:
    '''
    This is the body of rectangle class
    '''

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''return width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''to set the width value'''
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''return height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height to value'''
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
