import random
n = 10
d = {}

for i in range(1, n+1):
    for j in range(1, n+1):
        d[i, j] = random.randint(1, 9)
        print('%5d' % d[i, j], end="")
    print()
print("    ----------------------------------------------")
print("    ----------------------------------------------")
for i in range(1, n+1):
    for j in range(1, n+1):

        if i == 1: p1 = 1
        if i  > 1: p1 = i - 1
        if i == n: p2 = n
        if i  < n: p2 = i + 1

        if j == 1: r1 = 1
        if j >  1: r1 = j - 1
        if j == n: r2 = n
        if j <  n: r2 = j + 1

        t = 0
        for p in range(p1, p2 + 1):
            for r in range(r1, r2 +1):
                if not (p == i and r == j):
                    t += d[p, r]
        if t % 10 == d[i, j]:
            print(" -->%1d" % d[i, j], end="")
        else:
            print("%5d" % d[i, j], end="")
    print("")


