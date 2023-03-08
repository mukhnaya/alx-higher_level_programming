#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for pau in range(len(str)):
        if pau == n:
            str1[pau] = " "
        else:
            str1[pau] = str[pau]
    print(str1)
