#!/usr/bin/python3
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import sys
import os.path as pat
from sys import argv as k
'''adds arguments'''


my_file = "add_item.json"
new_list = []

if pat.exists(my_file):
    new_list = load_from_json_file(my_file)

for i in range(1, len(argv)):
    new_list.append(argv[i])

save_to_json_file(new_list, my_file)
