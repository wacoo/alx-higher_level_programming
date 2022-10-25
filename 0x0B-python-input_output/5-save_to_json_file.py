#!/usr/bin/python3
import json
"""Creates a function that data to json file"""


def save_to_json_file(my_obj, filename):
    """ write onject to file as json"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
