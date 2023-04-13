#!/usr/bin/python3
'''Save json string in file'''


import json


def save_to_json_file(my_obj, filename):
    '''
    Creates json file and save it in filename
    Args:
        my_obj (object): The python object (data struct)
        filename (str): The name to save the json file with
    Return:
        Not sure
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
