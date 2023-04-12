#!/usr/bin/python3
'''function that reads from a file'''


def read_file(filename=""):
    '''open a file'''
    with open(filename, encoding='utf-8') as mos:
        print(mos.read())
