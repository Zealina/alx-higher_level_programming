#!/usr/bin/python3
"""Can I add an attribute to you?"""


def add_attribute(obj, name, value):
    """Add an attribute to the object
    Args:
        obj (object): The object to try add attribute to
        name (string): The attriute to add
        value (unknown): The value of the attribute
    Return: Nothing if successful
        Raise a TypeError if unsucessful
    """

    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
