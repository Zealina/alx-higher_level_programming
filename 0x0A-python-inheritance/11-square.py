#!/usr/bin/python3
"""Holds the class that defines a square"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square and inherits from a Rectangle"""
    def __init__(self, size):
        """
        Instantiation of the square
        Args:
            size (int): The size of the square
        Return:
            Unclear
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Magic string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
