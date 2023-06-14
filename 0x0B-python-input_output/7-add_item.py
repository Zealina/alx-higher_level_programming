#!/usr/bin/python3
"""
This module contains functions that adds item from
command line argument to json notation
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

with open('add_item.json', 'r+', encoding='utf-8') as f:
    test_to_create = f.read()
new_list = []
if test_to_create == "":
    save_to_json_file(new_list, 'add_item.json')
new_list += load_from_json_file('add_item.json')
new_list.extend(sys.argv[1:])
save_to_json_file(new_list, 'add_item.json')
