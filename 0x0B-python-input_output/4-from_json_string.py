#!/usr/bin/python3
'''convert to json object'''


def from_json_string(my_str):
    '''function convert to JSON object'''
    import json
    return json.dumps(my_str)
