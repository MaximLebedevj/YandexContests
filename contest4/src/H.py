#!/usr/bin/env python3

n = int(input())
d = {}
for i in range(n):
    s = input().split()
    for porridge in s[1:]:
        if porridge in d.keys():
            d[porridge].append(s[0])
        else:
            d[porridge] = [s[0]]
input_type = input()
if input_type not in d.keys():
    print("Таких нет")
else:
    print(*sorted(d[input_type]), sep='\n')
