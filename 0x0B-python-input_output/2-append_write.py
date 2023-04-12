#!/usr/bin/python3
'''Open and append to a file'''


def append_write(filename="", text=""):
    '''Write text to an open file
    Args:
        filename (str): The name of the file
        text (str): Append into the file
    Return:
        The number of written characters
    '''
    with open(filename, 'a', encoding="UTF-8") as myfile:
        myfile.write(text)
    return len(text)
