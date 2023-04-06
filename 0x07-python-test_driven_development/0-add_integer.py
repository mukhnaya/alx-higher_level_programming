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


print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
