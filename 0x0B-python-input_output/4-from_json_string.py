#!/usr/bin/python3
"""Returns a object from json"""
import json


def from_json_string(my_str):
    """ json to object """
    return json.loads(my_str)
