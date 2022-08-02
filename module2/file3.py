# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:51:16 2021

@author: Sarah Cheung
"""

fname = input('Enter file name: ')
fh = open(fname)
lst = list()
for line in fh:
    word = line.split()
    for i in word:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
    