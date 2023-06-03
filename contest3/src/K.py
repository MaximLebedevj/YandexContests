#!/usr/bin/env python3

N = int(input())
arr = [""] * (N + 1)
for i in range(N + 1):
    arr[i] = input()
for i in range(N):
    if arr[i].lower().find(arr[N].lower()) != -1:
        print(arr[i])

