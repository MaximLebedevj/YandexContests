#!/usr/bin/env python3

#!/usr/bin/env python3

n = int(input())
dct = {}
for i in range(n):
    s = input()
    if s in dct.keys():
        dct[s] += 1
    else:
        dct[s] = 1

count = 0
for key in dct.keys():
    if dct[key] > 1:
        count += dct[key]
print(count)

