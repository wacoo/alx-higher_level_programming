#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ls = a_dictionary.copy()
    for x, y in a_dictionary.items():
        ls[x] = y * 2
    return ls
