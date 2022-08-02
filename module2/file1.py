# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:19:18 2021

@author: Sarah Cheung
"""

fname = input("Enter file name: ")
fh = open(fname)
text = fh.read()
print(text.upper())