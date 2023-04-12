#!/usr/bin/python3
'''creates object from JSON'''


def load_from_json_file(filename):
    '''this function'''
    import json
    with open(filename, encoding='utf-8') as mos:
        pau = mos.read()
        jos = json.loads(pau)
        return jos
