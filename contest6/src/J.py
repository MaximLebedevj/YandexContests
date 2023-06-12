from itertools import product

n = int(input())
print("А Б В")
s = product(range(1, n + 1), range(1, n + 1), range(1, n + 1),)
for i in s:
    if sum(i) == n:
        print(f'{i[0]} {i[1]} {i[2]}')

