#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        sr = str[:n] + str[n + 1:]
    else:
        sr = str[:]
    return sr
