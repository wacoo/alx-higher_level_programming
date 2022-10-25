#!/usr/bin/python3

""" Write a function that writes a string to a text """


def write_file(filename="", text=""):
    """ Write to file"""
    with open(filename, 'w', encoding="utf-8") as file1:
        return file1.write(text)
