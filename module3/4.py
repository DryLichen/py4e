# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 20:46:05 2021

@author: Sarah Cheung
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
time = int(input('Enter Count: '))
po = int(input('Enter position: '))
print(url)

for i in range(time):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[po-1].get('href')
    print(url)
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE  
  
url = input("Enter URL:")  
count = int(input("Enter count:"))  
position = int(input("Enter position:"))  
print(url)

for i in range(1,count+1):  
     html = urllib.request.urlopen(url,context=ctx).read()  
     soup = BeautifulSoup(html,"html.parser")  
     tags = soup('a')  
     url = tags[position-1].get('href')  
     print(url)
'''