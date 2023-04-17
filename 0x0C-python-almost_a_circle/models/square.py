#!/usr/bin/python3
"""This module contains properties of the class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class with properties of square, Inherits from Class Rectangle
    Args:
        Rectangle (class): The parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializations of the class Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.height

    @size.setter
    def size(self, size):
        """Size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """String representation of square"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.height))
