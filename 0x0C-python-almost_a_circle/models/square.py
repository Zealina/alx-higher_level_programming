#!/usr/bin/python3
"""This module contains properties of the class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class with properties of square, Inherits from Class Rectangle
    Args:
        Rectangle (class): The parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
        self.width = size
        self.height = size

    def __str__(self):
        """String representation of square"""
        return ("[Square] ({}) ({}/{}) -({}/{})".format
                (self.id, self.__x, self.__y, self.__width, self.__height))
