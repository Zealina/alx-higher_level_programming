#!/usr/bin/python3

def best_score(a_dictionary):
    bs = None
    if a_dictionary is None:
        return None
    for k in a_dictionary:
        if bs is None or bs < a_dictionary[k]:
            bs = a_dictionary[k]
    return bs
