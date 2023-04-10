#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        if(type(a) is float) | (type(b) is float):
            a = int(a)
            b = int(b)
            return a + b
        elif(type(a) is int) | (type(b) is int):
            return a + b
    except TypeError:
        if type(a) is not int:
            print("a must be an integer")
        if type(b) is not int:
            print("b must be an integer")
