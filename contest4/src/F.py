#!/usr/bin/env python3

n = int(input())
m = int(input())
a = set()
b = set()
for i in range(n + m):
    if (x := input()) in a:
        b.add(x)
    else:
        a.add(x)
res = a ^ b
if len(res) == 0:
    print("Таких нет")
else:
    res = sorted(list(res))
    print(*res, sep='\n')

