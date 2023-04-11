#!/usr/bin/python3
'''
Checks if an instance is of the same class
'''


def is_same_class(obj, a_class):
    '''Checks if "obj" is an instance of "a_class"
    Args:
        obj: the object
        a_class: The super or parent class
    Returns:
        True is obj is an exact instance of a_class
        otherwise, return false
    '''
    if type(obj) is a_class:
        return True
    return False
