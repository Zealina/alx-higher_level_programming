#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for x in a_dictionary:
        if x == key:
            a_dictionary[x] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
