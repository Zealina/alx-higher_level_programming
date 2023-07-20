#!/usr/bin/python3
"""This module contains function to print the pascal triangle"""


def pascal_triangle(n):
    """
    Function to print the pascal's triangle
    Args:
        n (int): The length of the triangle
    """
    triangle = []
    for i in range(n):
        if i == 0:
            row = [1]
            triangle.append(row)
            continue
        if i == 1:
            row = [1, 1]
            triangle.append(row)
            continue
        temp = [row[i] + row[i+1] for i in range(len(row) - 1)
        row = [1] + [temp] + [1]
        triangle.append(row)
    return triangle
