#!/usr/bin/python3

def roman_to_int(roman_string):
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if roman_string is None or roman_string == "":
        return 0
    new_list = []
    for x in roman_string:
        for k, v in a_dict.items():
            if k == x:
                new_list.append(v)
    if len(new_list) % 2 != 0:
        new_list.append(0)
    for n in range(0, len(new_list), 2):
        y = new_list[n]
        x = new_list[n + 1]

        result += (y + x) if y >= x else (x - y)
    return result


