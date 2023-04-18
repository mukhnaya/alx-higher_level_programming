#!/usr/bin/python3
from base import Base
'''Rectangle class'''


class Rectangle(Base):
    '''body of rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__()
        '''initialization class'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
