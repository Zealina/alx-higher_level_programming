#!/usr/bin/python3
"""
This module contains a function that deserializes a json
Notation and makes a python object
"""


import json


def load_from_json_file(filename):
    """
    Function to load from json file
    Args:
        filename (str): the name of the file to be deserialized
    Return:
        The deserialized object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
