#!/usr/bin/python3
''' this is the base class'''


class Base:
    '''body of base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''method for initialization of instance attributes'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
