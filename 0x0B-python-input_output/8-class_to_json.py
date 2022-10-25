#!/usr/bin/python3
""" convert class arguments to json file"""
import json


def class_to_json(obj):
    """ class to json """
    return obj.__dict__
