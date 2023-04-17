#!/usr/bin/python3
"""Rectangle, a subclass of base"""

from models.base import Base


class Rectangle(Base):
    """Defines the properties of a rectangle
    from inheriting from the clase Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of rectangle
        Args:
            width (int): The width of the recatangle
            height (int): The height of the rectangle
            x (int): The x axis
            y (int): The y axis
            id (int): The identigy of the instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for private attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for private attribute width"""
        self.setter_validation('width', width)
        self.__width = width

    @property
    def height(self):
        """Getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for private attribute height"""
        self.setter_validation('height', height)
        self.__height = height

    @property
    def x(self):
        """Getter for private attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for private attribute x"""
        self.setter_validation("x", x)
        self.__x = x

    @property
    def y(self):
        """Getter for private attribute x"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for private attribute y"""
        self.setter_validation("y", y)
        self.__y = y

    @staticmethod
    def setter_validation(attribute, value):
        """Validates the input before setting
        Args:
            attribute (str): The attribute to validate
            value (int): The value of said attribute
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(attribute))
        elif (attribute == 'x' or attribute == 'y'):
            if (value < 0):
                raise ValueError('{} must be >= 0'.format(attribute))
        elif (value <= 0):
            raise ValueError('{} must be > 0'.format(attribute))

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle based on width and height"""
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """The string describing the instance of the rectangle"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update the attributes of the instance
        Args:
            args (int): The arguments to be updated
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
