#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    lent = 0
    while lent < list_length:
        try:
            new_list.append(my_list_1[lent] / my_list_2[lent])
            lent += 1
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            lent += 1
        except IndexError:
            print("out of range")
            new_list.append(0)
            lent += 1
        except TypeError:
            print("wrong type")
            new_list.append(0)
            lent += 1
    return new_list

