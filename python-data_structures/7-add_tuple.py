#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = [0, 0]
    j = 0
    for num in tuple_a:
        if j < len(new_tuple):
            new_tuple[j] += num
        j += 1
    j = 0
    for num in tuple_b:
        if j < len(new_tuple):
            new_tuple[j] += num
        j += 1
    return tuple(new_tuple)
