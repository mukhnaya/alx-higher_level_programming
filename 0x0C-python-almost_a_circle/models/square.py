#!/usr/bin/python3
from models.base import Base
'''square class '''


class Square(Rectangle):
    '''body of square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, to_assign):
        self.size = to_assign
