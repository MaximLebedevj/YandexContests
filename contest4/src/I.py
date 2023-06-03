#!/usr/bin/env python3

objects = {}
while (x := input()) != '':
    s = x.split()
    for i in s:
        objects[i] = objects.get(i, 0) + 1
for i in objects.items():
    print(i[0], i[1])

