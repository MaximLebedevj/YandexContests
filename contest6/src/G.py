from itertools import combinations

n = int(input())
players = [input() for i in range(n)]
for i in combinations(players, 2):
    print(f'{i[0]} - {i[1]}')

