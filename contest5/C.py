n = int(input())
count = 0
k = 0
for i in range(1, n + 1):
    print(i, end=" ")
    count += 1
    if count > k:
        print()
        k = count
        count = 0

