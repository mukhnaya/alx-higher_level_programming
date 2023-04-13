#!/usr/bin/python3
import json
import sys
import os.path as p
from sys import argv as k

'''adds arguments'''
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_file = "add_item.json"
new_list = []

if p.exists(my_file):
    new_list = load_from_json_file(my_file)

for i in range(1, len(k)):
    new_list.append(k[i])

save_to_json_file(new_list, my_file)
