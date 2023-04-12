#!/usr/bin/python3
'''append string to a file'''


def append_write(filename="", text=""):
    '''function to append string, return len of string'''
    with open(filename, 'a', encoding='utf-8') as mos:
        mos.write(text)
    count = 0
    for i in text:
        count += 1
    return count
