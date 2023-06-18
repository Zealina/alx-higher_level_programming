#!/usr/bin/python3
"""
This module contains the properties of a square
"""

from models import rectangle


class Square(rectangle.Rectangle):
    """
    This class defines the properties of a triangle and inherits
    from class 'Rectangle' and it's parent classes
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of class 'Square'"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Reassigns values to the attributes"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """Return a dictionary representation of the square instance"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
