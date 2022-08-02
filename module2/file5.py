# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:23:31 2021

@author: Sarah Cheung
"""

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)
dic = {}
lst = list()
a = None
for line in fh:
    if line.startswith('From') and line[4] != ':':
        lst = line.split()
        word = lst[1]
        dic[word] = dic.get(word,0) + 1
for i,j in dic.items():
    if a is None:
        a = j
    elif j > a:
        a = j
        b = i
print(b,a)