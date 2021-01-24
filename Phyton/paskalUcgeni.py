

n = 20
d = {}
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            d[i, j] = 1
        else:
            d[i, j] = d[i - 1, j] + d[i - 1, j - 1]
        print("%6d" % d[i, j], end="")
    print()

