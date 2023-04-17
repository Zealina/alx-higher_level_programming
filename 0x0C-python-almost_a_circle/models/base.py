#!/usr/bin/python3
"""Almost a circle"""


class Base:
    """Class being defined in case of inheritance"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of class Base
        Args:
            id (int): The id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
