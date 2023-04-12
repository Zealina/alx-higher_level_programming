#!/usr/bin/python3
'''Creates class of base geometry'''


class BaseGeometry:
    '''A class called BaseGeometry'''

    def area(self):
        '''Raises an exception'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Checks if the value is an integer
        Args:
            name (str): The name associated with value
            value (int : The value associated with name

        Returns:
            Nothing, just checks for the value of "value
        '''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
