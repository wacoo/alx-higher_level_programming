#!/usr/bin/env python3
''' Same'''
from urllib import request
from sys import argv
from urllib import error
with request.urlopen(argv[1]) as res:
    try:
        pass
    except error.HTTPError as e:
        print(e.code)
