#!/usr/bin/python3
"""
Module contains a function that serializes an object into
a json file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function to serialize a json object to a file
    Args:
        my_obj (obj): python object to be serialized
        filename (str): file to serialize to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
