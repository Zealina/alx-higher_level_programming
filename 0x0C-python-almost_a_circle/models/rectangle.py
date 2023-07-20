#!/usr/bin/python3
"""
Module contains the properties for a rectangle
"""

from models import base


class Rectangle(base.Base):
    """
    Thiis class defines the attributes and methods of a
    rectangle
    It inherits from the 'Base' class in the 'base' module
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.setter_validation('width', value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.setter_validation('height', value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.setter_validation('x', value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.setter_validation('y', value)
        self.__y = value

    def setter_validation(self, set_name, value):
        """Setter validation"""
        if type(value) is not int:
            raise TypeError(set_name + ' must be an integer')
        if value < 0 and set_name in ['x', 'y']:
            raise ValueError(set_name + ' must be >= 0')
        elif value <= 0 and set_name in ['height', 'width']:
            raise ValueError(set_name + ' must be > 0')

    def area(self):
        """
        Function to find the area of the rectangle instance
        """
        return self.height * self.width

    def display(self):
        """
        Prints a representation of the rectangle to stdout
        """
        print('\n' * self.y, end="")
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        String reprepsentation of the Instance 'Rectangle'
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}]".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the value of the attributes of instance to '*args'"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns a dictionary representation of the Instance of
        'Rectangle'"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
