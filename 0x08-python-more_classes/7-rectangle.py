#!/usr/bin/python3
'''Rectangle declaration'''


class Rectangle:
    '''body of task 2'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        '''return width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width'''
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an intege")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''return height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set hieght'''
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        '''get area'''
        return self.__width * self.__height

    def perimeter(self):
        '''return perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for pau in range(self.__height - 1):
                for mos in range(self.__width - 1):
                    print(str(self.print_symbol), end="")
                print()
        return str(self.print_symbol) * self.__width

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
