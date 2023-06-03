#!/usr/bin/env python3

n = int(input())
for i in range(0, n):
    s = input()
    pos = s.find("зайка")
    if (pos != -1):
        print(pos + 1)
    else:
        print("Заек нет =(")

