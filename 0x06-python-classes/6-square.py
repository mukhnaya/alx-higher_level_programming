#!/usr/bin/python3
'''class square'''


class Square:
    '''body of class square'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''return size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set value to size'''

        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        '''return position'''

        return self.__position

    @position.setter
    def position(self, value):
        '''set values to position'''

        self.__position = value
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''return area of square'''

        return self.__size * self.__size

    def my_print(self):
        '''print square'''

        if self.__position:
            if self.__size > 0:
                print('\n' * self.position[1], end="")
                for pau in range(self.__size):
                    print(' ' * self.position[0], end="")
                    print('#' * self.size)
        if self.__size == 0:
            print()
