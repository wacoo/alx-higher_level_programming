#!/usr/bin/env python3
import urllib.request

with urllib.request.urlopen('http://gugemt.tech') as response:
    html = response.read()
    #print(html)
