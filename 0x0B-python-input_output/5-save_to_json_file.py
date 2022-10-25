#!/usr/bin/python3
"""Creates a function that data to json file"""
import json


def save_to_json_file(my_obj, filename):
    """ write onject to file as json"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
