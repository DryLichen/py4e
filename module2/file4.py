# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:51:28 2021

@author: Sarah Cheung
"""

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)
lst = list()
count = 0
for line in fh:
    if line.startswith('From') and line[4] !=  ':':
        lst = line.split()
        word = lst[1]
        count = count + 1
        print(word)
print('There were',count,'lines in the file with From as the first word')