# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:18:27 2021

@author: Sarah Cheung
"""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        total = total + float(line[line.find(':')+1:].strip())
aver = total/count   
print("Average spam confidence:",aver)

        