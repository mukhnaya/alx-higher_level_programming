#!/usr/bin/python3
'''write text to a file
and return size of string written
'''


def write_file(filename="", text=""):
    '''write text and return size of text'''
    with open('filename', 'w', encoding='utf8') as mos:
        mos.write(text)
    count = 1
    for i in text:
        count +=1
    return count
