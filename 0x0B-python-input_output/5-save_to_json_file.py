#!/usr/bin/python3
'''write json object to file'''


def save_to_json_file(my_obj, filename):
    '''save json to file'''
    import json
    mos = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as pa:
        pa.write(mos)
