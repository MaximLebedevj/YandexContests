n = int(input())
res = ""
for i in range(n):
    num = int(input())
    maxx = 0
    while num > 0:
        x = num % 10
        num //= 10
        if x > maxx:
            maxx = x
    res += str(maxx)
print(res)

