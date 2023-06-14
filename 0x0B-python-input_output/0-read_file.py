#!/usr/bin/python3
"""Module to Read a file"""

def read_file(filename=""):
    """
    Function to read a file and print it out
    
    Args:
        filename (str): The name of the file to be read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        new = f.read()
        print(new, end="")
