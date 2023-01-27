#!/usr/bin/env python3
''' Fetch a given url using urllib '''


from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    #print(response.headers.items())
    r = response.read()
    print('Body response:')
    print('\t- type:', type(r))
    print('\t- content:', r)
    print('\t- utf8 content:', r.decode('utf-8'))
    
