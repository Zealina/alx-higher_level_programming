#!/usr/bin/python3

def roman_to_int(roman_string):
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    if roman_string is None or roman_string == "":
        return 0
    for i in range(len(roman_string)):
        for j in a_dict:
            if roman_string[i] == j:
                if i != 0 and roman_string[i - 1] 
                res += a_dict[j]
    return res
