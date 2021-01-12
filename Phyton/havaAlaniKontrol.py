import random
import math
n = 10
d = {}
u = {}

for i in range(1, n + 1):
    for j in range(1, n + 1):
        x1 = random.randint(1, 999)
        y1 = random.randint(1, 999)
        durum = random.randint(0, 1)
        d[i, j] = [x1, y1, durum]
        print('  [%3d,%3d,%1d]' % (d[i, j][0], d[i, j][1], d[i, j][2]), end='')
    print()
print("  --------------------------------------------------------------------------------------------------------------------------------")
print("  --------------------------------------------------------------------------------------------------------------------------------")

ri = random.randint(1, n)
rj = random.randint(1, n)
durum = d[ri, rj][2]
while durum == 0:
    ri = random.randint(1, n)
    rj = random.randint(1, n)
    durum = d[ri, rj][2]

print(ri, rj)

print("  --------------------------------------------------------------------------------------------------------------------------------")
x1 = d[ri, rj][0]
y1 = d[ri, rj][1]
k = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        x2 = d[i, j][0]
        y2 = d[i, j][1]
        durum = d[i, j][2]
        uzaklik = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        k += 1
        u[k] = [ri, rj, x1, y1, i, j, x2, y2, uzaklik, durum]
        print("%3d %3d [%3d,%3d] %3d %3d [%3d,%3d] uzaklik :%10.4f durum : %1d" % (u[k][0], u[k][1], u[k][2], u[k][3], u[k][4], u[k][5], u[k][6], u[k][7], u[k][8], u[k][9]))

print("  --------------------------SIRALIYOR...-------------------------")
for i in range(1, k):
    for j in range(i + 1, k + 1):
        if u[i][8] > u[j][8]:
            g = u[i][0] ; u[i][0] = u[j][0] ; u[j][0] = g
            g = u[i][1] ; u[i][1] = u[j][1] ; u[j][1] = g
            g = u[i][2] ; u[i][2] = u[j][2] ; u[j][2] = g
            g = u[i][3] ; u[i][3] = u[j][3] ; u[j][3] = g
            g = u[i][4] ; u[i][4] = u[j][4] ; u[j][4] = g
            g = u[i][5] ; u[i][5] = u[j][5] ; u[j][5] = g
            g = u[i][6] ; u[i][6] = u[j][6] ; u[j][6] = g
            g = u[i][7] ; u[i][7] = u[j][7] ; u[j][7] = g
            g = u[i][8] ; u[i][8] = u[j][8] ; u[j][8] = g
            g = u[i][9] ; u[i][9] = u[j][9] ; u[j][9] = g
m = 0
for i in range(1, k + 1):
    if u[i][9] == 1:
        m += 1
        print("SN :%3d Adet :%3d %3d %3d [%3d,%3d] %3d %3d [%3d,%3d] uzaklik :%10.4f durum : %1d" % (i, m, u[i][0], u[i][1], u[i][2], u[i][3], u[i][4], u[i][5], u[i][6], u[i][7], u[i][8], u[i][9]))
