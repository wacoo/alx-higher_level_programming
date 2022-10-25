#!/usr/bin/python3

""" Write a function that reads text file using UTF-8"""


def read_file(filename=""):
    """read file"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end='')
