#!/usr/bin/python3
'''This module contains a class called rectangle'''


class Rectangle:
    '''Defines the properties of a rectangle

    Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError('height must be >= 0')
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compares the size of two rectangles'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        area_1 = rect_1.height * rect_1.width
        area_2 = rect_2.height * rect_2.width
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    def area(self):
        '''Returns the area of a rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''Returns the perimeter of a rect'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''String representation of rectangle'''
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            ret_str += str(self.print_symbol) * self.__width
            if i + 1 < self.__height:
                ret_str += '\n'
        return ret_str

    def __repr__(self):
        '''Returns the string representation of Rectangle'''
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        '''Prints a message to show deletion of an instance'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        '''Return square as rectangle'''
        return cls(size, size)
