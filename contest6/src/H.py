from itertools import cycle

m = int(input())
names = [input() for i in range(m)]
n = int(input()) 
count = 0
for names in cycle(names):
    if count < n:
        print(names)
        count += 1
    else:
        break

