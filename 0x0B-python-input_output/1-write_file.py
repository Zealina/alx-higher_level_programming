#!/usr/bin/python3
'''Open and write to a file'''


def write_file(filename="", text=""):
    '''Write text to an open file
    Args:
        filename (str): The name of the file
        text (str): Write into the file
    Return:
        The number of written characters
    '''
    with open(filename, mode='w', encoding="UTF-8") as myfile:
        myfile.write(text)
    return len(text)
