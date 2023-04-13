#!/usr/bin/python3
'''Search for string and append after string'''


def append_after(filename="", search_string="", new_string=""):
    '''Open file, search for string and append newstring
    Args:
        filename (str): The name of the file
        search_string (str): The string to search for
        new_string (str): The string to append after
    '''
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if line.find(search_string) != -1:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.write("".join(lines))
