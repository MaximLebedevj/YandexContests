#!/usr/bin/env python3

str1 = input()
str2 = input()
a = set()
b = set()
for i in str1:
    a.add(i)
for i in str2:
    b.add(i)
c = a & b
print(*c, sep='')

