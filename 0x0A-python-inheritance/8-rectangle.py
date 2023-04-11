#!/usr/bin/python3
'''rectangle inherits from base geometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''body of rectangle class'''
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
