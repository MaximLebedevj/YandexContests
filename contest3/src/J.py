#!/usr/bin/env python3

dct = {}
s = input()
while s != "ФИНИШ":
    s = s.lower()
    for i in s:
        if i.isalpha():
            dct[i] = dct.get(i, 0) + 1
    s = input()
print(max(sorted(dct), key=lambda x: dct[x]))

