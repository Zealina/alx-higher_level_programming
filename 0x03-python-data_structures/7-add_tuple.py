#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a[0]:
        tuple_a[0] = 0
    if not tuple_a[1]:
        tuple_a[1] = 0
    if not tuple_b[0]:
        tuple_b[0] = 0
    if not tuple_b[1]:
        tuple_b[1] = 0
    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))