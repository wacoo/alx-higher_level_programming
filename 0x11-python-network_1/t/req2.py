#!/usr/bin/env python3
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://gugemt.tech') as response:
	with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
		shutil.copyfileobj(response, tmp_file)
with open('/tmp/t) as html:
	print(html.read())
