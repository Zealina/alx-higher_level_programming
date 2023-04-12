#!/usr/bin/python3
"""Defines a rectangle based on class BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation of the rectangle
        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        Returns:
            Inherits the returns from superclass BaseGeometry
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Magic string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
