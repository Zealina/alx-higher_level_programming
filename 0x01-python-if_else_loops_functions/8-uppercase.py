#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        new = ord(str[i])
        if (new >= ord('a')) and (new <= ord('z')):
            new -= 32
        print("{:c}".format(new), end="")
    print("\n", end="")
