#!/usr/bin/python3
"""
This module contains a function that appends a string to
the end of a file
"""


def append_write(filename="", text=""):
    """
    Function to append a string to the end of a file
    Args:
        filename (str): The name of the file to be appended to
        text (str): String to append to end of file

    Return:
        The number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
