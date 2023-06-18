#!/usr/bin/python3
"""This module contains the base class for all other works on
this project
"""

import json
import turtle


class Base:
    """
    This class defines the base properties of a shape
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes an instance of the class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of a dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json representation of 'list_objs' to a file"""
        dict_list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())
        string = cls.to_json_string(dict_list)
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a deserialized json string into a dictionary
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class with the data of dictionary
        """
        dummy = cls(2, 2, 2, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances created from a file dictionary
        """
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                deserialized = Base.from_json_string(f.read())
            return [cls.create(**inst) for inst in deserialized]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a file to csv instead of json"""
        list_csv = []
        for obj in list_objs:
            a = cls.to_dictionary(obj)
            if cls.__name__ == 'Square':
                temp = "{},{},{},{}".format(a['id'], a['size'], a['x'], a['y'])
            elif cls.__name__ == 'Rectangle':
                temp = "{},{},{},{},{}".format(a['id'], a['width'],
                                               a['height'], a['x'], a['y'])
            list_csv.append(temp)
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as f:
            f.write('\n'.join(list_csv))

    @classmethod
    def load_from_file_csv(cls):
        """load an instance from a file"""
        with open(cls.__name__ + '.csv', 'r', encoding='utf-8') as f:
            my_list = []
            for line in f.readlines():
                values = line.strip().split(',')
                if cls.__name__ == 'Square':
                    keys = ['id', 'size', 'x', 'y']
                elif cls.__name__ == 'Rectangle':
                    keys = ['id', 'width', 'height', 'x', 'y']
                values = [int(x) for x in values]
                my_dict = dict(zip(keys, values))
                my_list.append(my_dict)
        return [cls.create(**my_dict) for my_dict in my_list]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw  squares and rectangles using the python turtle
        module
        """
        turtle.penup()
        turtle.pensize(10)
        turtle.bgcolor("yellow")
        turtle.color("teal")
        turtle.hideturtle()
        turtle.goto(-300, 300)
        turtle.speed(0)

        for instance in list_rectangles:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 200
            else:
                move_by = instance.width + 30
                x_coordinate = round(turtle.xcor(), 5)
                turtle.goto(x_coordinate + move_by, 300)
        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_coordinate = round(turtle.xcor(), 5)
            turtle.goto(x_coordinate + move_by, 100)
        turtle.exitonclick()
