#!/usr/bin/python3
"""Almost a circle"""


import json


class Base:
    """Class being defined in case of inheritance"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of class Base
        Args:
            id (int): The id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation of the dictionaries
        Args:
            list_dictionaries (dict): The list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_obj):
        """Save json string documentation to file
        Args:
            list_obj (object): Contains the list of all instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='UTF-8') as fd:
            if list_obj is None or list_obj == []:
                fd.write('[]')
                return
            workwith = [work.to_dictionary() for work in list_obj]
            fd.write(cls.to_json_string(workwith))
