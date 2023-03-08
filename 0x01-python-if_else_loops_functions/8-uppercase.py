#!/usr/bin/python3
def uppercase(str):
    final_string = ''
    for pau in range(len(str)):
        if pau in 'abcdefghijklmnopqrstuvwqxyz':
            mos = ord(pau)
            jul = mos - 32
            final_string = final_string + chr(jul)
        else:
            final_string = final_string + pau
    print("{}".format(final_string))
