#!/usr/bin/python3

""" Write a function that writes a string to a text file

        Args:
            filename: name of the file being written to
            text: the string to be written to the file
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as file1:
        return file1.write(text)
