#!/usr/bin/python3
import json
"""Returns a object from json"""


def from_json_string(my_str):
    """ json to object """
    return json.loads(my_str)
