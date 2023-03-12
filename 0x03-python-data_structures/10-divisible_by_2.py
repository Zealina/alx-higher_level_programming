#!/usr/bin/python3
import sys

def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if (i % 2 == 0):
            new_list.append(1)
        else:
            new_list.append(0)
    print("The size of new_list: ", sys.getsizeof(new_list))
    print("The size of old list: ", sys.getsizeof(my_list))
    return new_list
