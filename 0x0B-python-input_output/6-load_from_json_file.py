#!/usr/bin/python3
import json
"""Defines a function that loads object from json file"""


def load_from_json_file(filename):
    with open(filename, 'r') as fl:
        return json.load(fl)
