#!/usr/bin/python3
import json
""" convert class arguments to json file"""


def class_to_json(obj):
    return obj.__dict__
