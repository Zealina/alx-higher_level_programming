#!/usr/bin/python3
'''This modeule defines a class called students'''


class Student:
    '''Defines a student data'''
    def __init__(self, first_name, last_name, age):
        '''Instantiate the class Student
        Args:
            first_name: The first name of the student
            last_name: The student' last name
            age: Age of student
        Return:
            None
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns the dictionary reprsentation of instance'''
        return self.__dict__
