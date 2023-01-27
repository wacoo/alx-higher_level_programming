#!/usr/bin/env python3
''' Same'''
import requests
from sys import argv
data = {'email:' argv[2]}
r = requests.post(argv[1], params = data)
print("Your email is: {}".format(r.text))
