#!/usr/bin/python3
'''Convert object to json string'''


import json


def to_json_string(my_obj):
    '''
    Returns the json representation of my_obj
    Args:
        my_obj (object): The object to convert to json string
    Returns:
        None
    '''
    ret_string = json.dumps(my_obj)
    return ret_string
