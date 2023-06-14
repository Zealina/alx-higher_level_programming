#!/usr/bin/python3
"""
This module contains function to convert a python class to dict
"""


def class_to_json(obj):
    """
    Function that represents a python class instance as a dict
    Args:
    obj (obj):
        The object to be converted to dict
    """
    return obj.__dict__
