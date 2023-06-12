n = int(input())
winner = ""
maxx = 0
count = 0
for i in range(n):
    count = 0
    name = input()
    number = int(input())
    while number > 0:
        count += number % 10
        number //= 10
    if count >= maxx:
        maxx = count
        winner = name
print(winner)

