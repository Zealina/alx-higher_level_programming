#!/usr/bin/python3
"""
This module contains function that loads an object
from a json string
"""

import json


def from_json_string(my_str):
    """
    Returns a python object by deserializing a json string
    Args:
        my_str (str): json string to be deserialized
    """
    return json.loads(my_str)
