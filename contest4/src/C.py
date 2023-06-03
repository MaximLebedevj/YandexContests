#!/usr/bin/env python3

n = int(input())
dct = {}
for i in range(n):
    s = input().split()
    for word in s:
        if word in dct.keys():
            dct[word] = 1
        else:
            dct[word] = []

count = 0
for key in dct.keys():
    print(key)

