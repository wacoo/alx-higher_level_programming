#!/usr/bin/python3

""" a function that appends a string to a file """


def append_write(filename="", text=""):
    """ Append to file"""
    with open(filename, 'a+', encoding="utf-8") as f:
        return f.write(text)
