#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for x in set(my_list):
        res += x
    return res
