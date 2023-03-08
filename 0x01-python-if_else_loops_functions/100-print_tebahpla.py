#!/usr/bin/python3

for i in reversed(range(0, 26)):
    print("{:c}".format((i + ord('A')) if not(i % 2) else (i + ord('a'))), end = "")
