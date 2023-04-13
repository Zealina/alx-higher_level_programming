#!/usr/bin/python3
'''Load python object from json file'''


import json


def load_from_json_file(filename):
    '''Load python object from json file
    Args:
        filename (str): The name of the json file to load from
    Return:
        The python object
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        ret_obj = json.load(f)
    return ret_obj
