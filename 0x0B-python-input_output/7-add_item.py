#!/usr/bin/python3
import json
import sys
from os.path import exists
""" Adds arguments to a list and saves to file"""

if __name__ == "__main__":
    save_to_json_file = \
        __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file =\
        __import__("6-load_from_json_file").load_from_json_file

    if exists("add_item.json"):
        lst = load_from_json_file("add_item.json")
    else:
        lst = []
    lst.extend(sys.argv[1:])
    save_to_json_file(lst, "add_item.json")
