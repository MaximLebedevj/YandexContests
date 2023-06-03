#!/usr/bin/env python3

s = input()
a = set()
for i in s:
    a.add(i)
print(*a, sep='')

