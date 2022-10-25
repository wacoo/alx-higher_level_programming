#!/usr/bin/python3
"""Defines a function that loads object from json file"""
import json


def load_from_json_file(filename):
    """ load json file """
    with open(filename, 'r') as fl:
        return json.load(fl)
