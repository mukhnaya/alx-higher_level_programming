#!/usr/bin/python3
def uppercase(str):
    for pau in range(len(str)):
        if str[pau] >= 'a' and str[pau] <= 'z':
            mos = str[pau]
            mos = ord(mos)
            mos = mos - 32
            mos = chr(mos)
            str = str[:pau] + mos + str[pau + 1:]
