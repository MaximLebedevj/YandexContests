n = int(input())
count = 0
for i in range(n):
    cin = input()
    for j in range(len(cin)):
        count += int(cin[j])
print(count)

