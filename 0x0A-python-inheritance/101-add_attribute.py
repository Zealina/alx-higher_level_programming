#!usr/bin/python3
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
    try:
        obj.(name) = value
    except AttributeError:
        raise TypeError("can't add new attribute")
