#!/usr/bin/env python3

import sys
from urllib import request
with request.urlopen(sys.argv[1]) as res:
	r = res.getheader('X-Request-Id')
	print(r)
