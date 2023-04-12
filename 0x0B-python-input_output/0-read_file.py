#!/usr/bin/python3
'''
Read a file and print it to standard output
'''


def read_file(filename=""):
    ''' Read file from filename and print to stdout 
    Args:
        filename (str): The name of the file to be printed
    Return:
        None
    '''
    with open(filename, 'r', encoding="UTF-8") as myfile:
        print(myfile.read())
