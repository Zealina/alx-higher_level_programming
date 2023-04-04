#!/usr/bin/python3
'''This module contains a class called rectangle'''


class Rectangle:
    '''Defines the properties of a rectangle

    Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    '''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value
