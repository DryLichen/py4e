# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:48:12 2021

@author: Sarah Cheung
"""

import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #生成链接
    address = input('Enter location: ')
    if len(address) < 1:
        break
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    paras = dict()
    paras['key'] = 42
    paras['address'] = address
    url = serviceurl + urllib.parse.urlencode(paras)
    
    #解析数据
    print('Retrieving: ',url)
    hd = urllib.request.urlopen(url, context=ctx).read().decode()
    print('Retrieved',len(hd),'characters')
    data = json.loads(hd)
    
    if not data or 'status' not in data or data['status'] != 'OK':
        print('----------------Fail to Retrieve----------------')
        print(data)
        continue
    
    print(json.dumps(data,indent=4))
    
    placeid = data['results'][0]['place_id']
    print('Place id ', placeid)