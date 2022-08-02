# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:21:09 2021

@author: Sarah Cheung
"""

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
    
with open(fname) as handle:
    dic = {}
    lst2 = list()
    for line in handle:
        if line.startswith('From') and line[4] != ':':
            lst = line.split()
            wds = lst[5]
            w = wds.split(':')
            hrs = w[0]
            dic[hrs] = dic.get(hrs,0) + 1
            
    for k,v in dic.items():
        lst2.append((k,v))
        lst2.sort()
    
    for i in lst2:
        print(i[0],i[1])
        

