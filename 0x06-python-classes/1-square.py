#!/usr/bin/python3
"""Define a square of size 'size'"""


class Square:
    """ This class contains information about a
    square"""
    def __init__(self, size=0):
        """The initialization method of the Square class

        Args:
            size (int): The size of the square
        """
        self.__size = size
