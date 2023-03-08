#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        new = ord(str[i])
        if (new >= ord('a')) and (new <= ord('z')):
            new -= 32
        print(f"{new:c}", end = "")
    print("\n", end = "")
