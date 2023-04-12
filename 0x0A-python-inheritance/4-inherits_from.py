#!/usr/bin/python3
'''
Checks for the inheritance of an object
'''


def inherits_from(obj, a_class):
    '''
    Checks if obj inherits from a_class on any level
    Args:
        obj: The object to check for
        a_class: The potential superclass
    Return: True if obj is a subclass of a_class, false otherwise
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
