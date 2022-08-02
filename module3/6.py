# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:21:33 2021

@author: Sarah Cheung
"""

import urllib.request, urllib.error, urllib.parse
import ssl
import json

#设置证书
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
hd = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(hd), 'characters')

data = json.loads(hd)
lst = list()
for i in data['comments']:
    lst.append(int(i['count']))
print('Count: ',len(lst))
print('Sum: ', sum(lst))