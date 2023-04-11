#!/usr/bin/python3
'''
Checks for the parent of an object
'''


def is_kind_of_class(obj, a_class):
    '''
    Checks if obj is an instance of a_class on any level
    Args:
        obj: The object to check for
        a_class: The potential superclass
    Return: True if obj is a member of a_class, false otherwise
    '''
    if isinstance(obj, a_class):
        return True
    return False
