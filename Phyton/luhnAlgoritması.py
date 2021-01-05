

def luhnAlgoritmasi(s):
    n = 16
    d1 = {}
    d2 = {}
    for i in range(1, n+1):
        d2[i] = int(s[i-1])
    for i in range(1, n+1):
        if i % 2 != 0:
            d1[i] = 2 * d2[i]
            if d1[i] > 9:
                d1[i] = int(d1[i]/10) + d1[i] % 10

        else:
            d1[i] = d2[i]
    teklerToplami = 0
    ciftlerToplami = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            teklerToplami += d1[i]
        else:
            ciftlerToplami += d1[i]

    toplam = ciftlerToplami + teklerToplami

    kalan = toplam % 10
    if kalan == 0:
        return True
    else:
        return False

s = "5492968795874876"

if luhnAlgoritmasi(s) == True:
    print(s + ": BU KART NO GEÇERLİDİR ")
else:
    print(s + ": BU KART NO GEÇERİ DEĞİLİDİR")

for i in range(0, 100):
    i = i + 1
    print(i)
