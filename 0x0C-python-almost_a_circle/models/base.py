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

    @staticmethod
    def from_json_string(json_string):
        """Convert json string to python code
        Args:
            json_string (str): The string to be converted
        Returns:
            The converted python code
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of the class
        Args:
            dictionary (kwargs): A list of keyworded args as dict
        Returns:
            An instance with attributes from dictionary
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance
