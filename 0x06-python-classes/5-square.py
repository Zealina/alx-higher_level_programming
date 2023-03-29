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
        self.size = size

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ area: Calculate the area of a square from size
        Return: the Area
        """
        return self.__size ** 2

    def my_print(self):
        """print the square from size"""
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
