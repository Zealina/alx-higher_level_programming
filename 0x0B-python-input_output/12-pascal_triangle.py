#!/usr/bin/python3
'''Define a function that calculates the pascals triangle'''


def pascal_triangle(n):
    '''Calculate the pascals triangle
    Args:
        n (int): number of levels
    '''
    if n <= 0:
        return []
