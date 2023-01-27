#!/usr/bin/env python3
''' Accept url and email and disply email '''


import requests
from sys import argv

data = {'email:' argv[2]}
r = requests.post(argv[1], data=data)
print(r.text)
