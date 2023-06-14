#!/usr/bin/python3
"""
This module defines a class 'student'
"""


class Student:
    """
    This class defines the attributes of a student
    Args:
        first_name (str): The firstname of the student
        last_name (str): The lastname of said student
        age (int): The age of the student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the attributes of class
        'Student'"""
        return self.__dict__
