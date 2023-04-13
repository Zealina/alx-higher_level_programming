#!/usr/bin/python3
'''Convert strings from json to python representation'''


import json


def from_json_string(my_str):
    '''
    Convert string from json to python repr
    Args:
        my_str (str): The json representation
    Return:
        The python representation
    '''
    ret_obj = json.loads(my_str)
    return ret_obj
