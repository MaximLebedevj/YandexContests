n = int(input())
count = 0
res = 0
end_count = 0
while end_count != n:
    cin = input()
    if cin == "ВСЁ":
        end_count += 1
        res += count
        count = 0
    if cin == "зайка":
        count = 1
print(res)

