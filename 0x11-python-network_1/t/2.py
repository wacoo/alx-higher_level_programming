#!/usr/bin/env python3
''' accept email address a prameter amd display it urllib'''


from urllib import request, parse
from sys import argv
value = {'email': argv[2]}
data = parse.urlencode(value)
data = data.encode('ascii')
req = request.Request(argv[1], data)
with request.urlopen(req) as res:
	print('Your email is: {}'.format(res.decode('utf-8')))
