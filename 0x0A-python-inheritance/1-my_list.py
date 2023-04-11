#!/usr/bin/python3
'''
Create a Class MyList
'''


class MyList(list):
    '''Class, a subclass of list'''
    def __init__(self, my_list=[]):
        '''Initialize an instance of class'''
        self.my_list = my_list

    def print_sorted(self):
        '''Print sorted list'''
        print(sorted(self))
