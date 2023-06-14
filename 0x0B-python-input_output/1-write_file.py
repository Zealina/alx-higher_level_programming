#!/usr/bin/python3
"""
This module contains function to write a string to a text file
"""


def write_file(filename="", text=""):
    """
    Function to write a string to a text file
    Args:
        filename (str): The name of the file to be written to
        text (str): The text to be written into the file
    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_of_char = f.write(text)
        return(num_of_char)
