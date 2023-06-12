n = int(input())
k = 3
for i in range(1, n + 1):
    for j in range(k, 0, -1):
        print("До старта", j, "секунд(ы)")
    print("Старт " + str(i) + "!!!")
    k += 1

