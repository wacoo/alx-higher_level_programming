#!/usr/bin/python3
def no_c(my_string):
    new_s = ""
    for x in range(len(my_string)):
        if my_string[x] != "c" and my_string[x] != "C":
            new_s += my_string[x]
    return new_s
