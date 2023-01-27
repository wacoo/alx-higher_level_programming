#!/usr/bin/env python3
''' Same'''
import requests
from sys import argv

r = requests.get(argv[1])
print(r.headers['X-Request-Id'])
