def gcd(n: int, q: int) -> int:
    if q == 0:
        return n
    return gcd(q, n % q)


a = []
n = int(input())
for i in range(n):
    x = int(input())
    if i < 2:
        a.append(x)
        continue
    a[0] = gcd(a[0], a[1])
    a[1] = x

a[0] = gcd(a[0], a[1])

print(a[0])


