#!/usr/bin/python3
def weight_average(my_list=[]):
    n = 0
    s = 0
    if len(my_list) == 0:
        return 0
    for x in my_list:
        for y in range(len(x)):
            n = n + (x[0] * x[1])
            s = s + x[1]
    return n/s
