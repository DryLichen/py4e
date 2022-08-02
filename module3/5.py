# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:48:09 2021

@author: Sarah Cheung
"""

import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
fh = urllib.request.urlopen(url, context=ctx)
data = fh.read()

#fromstring 将string转化为xml tree
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('Count: ', len(lst))
rlst = list()
for i in lst:
    rlst.append(int(i.find('count').text))
print('Sum: ', sum(rlst))