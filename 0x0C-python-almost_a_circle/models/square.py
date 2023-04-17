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

    def update(self, *args, **kwargs):
        """Updates the value of square attributes
        Args:
            args (int): ints to update attributes with
            kwargs (dict): Keyworded args to update attributes with
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
