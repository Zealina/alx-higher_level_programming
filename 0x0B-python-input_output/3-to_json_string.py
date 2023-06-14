#!/usr/bin/python3
"""
This module contains a function to write a JSON representation
of an object
"""

import json


def to_json_string(my_obj):
    """
    Serializes an object into a json string
    Arg:
        my_obj: the object to be serialized
    Return:
        The json representation of the object
    """
    return json.dumps(my_obj)
