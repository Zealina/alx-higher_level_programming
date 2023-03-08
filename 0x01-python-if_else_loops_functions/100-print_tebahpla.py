#!/usr/bin/python3

for i in reversed(range(0, 26)):
    c = ord('A')
    d = ord('a')
    print("{:c}".format((i + c) if not (i % 2) else (i + d)), end="")
