#!/usr/bin/python3
"""Almost a circle"""


import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """Create an instance from a file"""
        try:
            with open(cls.__name__ + ".json", 'r', encoding='utf-8') as fd:
                json_string = cls.from_json_string(fd.read())
        except FileNotFoundError:
            return []
        return [cls.create(**new) for new in json_string]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Convert dict to csv and save in file
        Args:
            list_objs (list): List of instances
        """
        with open(cls.__name__ + ".csv", 'w', encoding='utf-8') as fd:
            writer = csv.writer(fd)
            for obj in list_objs:
                s = cls.to_dictionary(obj)
                if cls.__name__ == "Rectangle":
                    rect_list = [s['id'], s['width'],
                                 s['height'], s['x'], s['y']]
                elif cls.__name__ == "Square":
                    rect_list = [s['id'], s['size'], s['x'], s['y']]
                writer.writerow(rect_list)

    @classmethod
    def load_from_file_csv(cls):
        """Convert csv to dict"""
        with open(cls.__name__ + ".csv", newline='') as fd:
            reader = csv.reader(fd)
            my_list = []
            for row in reader:
                s = [int(i) for i in row]
                if cls.__name__ == "Rectangle":
                    new_dict = {'id': s[0], 'width': s[1], 'height':s[2],
                                'x': s[3], 'y': s[4]}
                if cls.__name__ == "Square":
                    new_dict = {'id': s[0], 'size': s[1], 'x': s[2],
                                'y': s[3]}
                my_list.append(new_dict)
                return [cls.create(**new) for new in my_list]
