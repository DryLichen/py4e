'''import re

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'Actual data.txt'
with open(fname) as handle:
    word = handle.read()
    lst = re.findall('[0-9]+', word)
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    tot = sum(lst)
print(tot)'''

#列表解析 list comprehension
import re
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'Actual data.txt'
with open(fname) as handle:
    print(sum([int(i) for i in re.findall('[0-9]+',handle.read())]))