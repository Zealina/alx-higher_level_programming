#!/usr/bin/python3
'''This module contains a class called rectangle'''


class Rectangle:
    '''Defines the properties of a rectangle'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        '''Getter for width'''
        return self.__width

    def width(self, value):
        '''Setter for width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    def height(self):
        '''Getter for height'''
        return self.__height

    def height(self, value):
        '''Setter for height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value
