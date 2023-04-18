#!/usr/bin/python3
from models.base import Base
'''Rectangle class'''


class Rectangle(Base):
    '''body of rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialization class'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''returns width'''
        return self.__width

    @width.setter
    def width(self, to_assign):
        if type(to_assign) != int:
            raise TypeError("width must be an integer")
        if to_assign <= 0:
            raise ValueError("width must be greater than zero")
        self.__width = to_assign

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, to_assign):
        if type(to_assign) != int:
            raise TypeError("height must be an integer")
        if to_assign <= 0:
            raise ValueError("height must be greather tha zero")
        self.__height = to_assign

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, to_assign):
        if to_assign < 0:
            raise ValueError("x must be >= 0")
        self.__x = to_assign

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, to_assign):
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y

    def area(self):
        return self.__width * self.__height
