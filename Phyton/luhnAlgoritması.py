import os
import sys

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
def sonDigitDogrulama(s):
    n=16
    d1={}
    d2={}
    for i in range(1, n+1):
        d2[i] = int(s[i - 1])
    for i in range(1, n):
        d1[i] = d2[n-i]
    for i in range(1, n):
        if i % 2 != 0:
            d1[i] = 2*d1[i]
            if d1[i] > 9:
                 d1[i] -= 9
    toplam=0
    for i in range(1, n):
        toplam += d1[i]

    kalan = 9 * toplam % 10
    if kalan == d2[n]:
        return True, kalan
    else:
        return False, -1

s = "4506347004318099"
print("------------Luhn Algoritması------------")
if luhnAlgoritmasi(s) == True:
    print(s + ": BU KART NO GEÇERLİDİR ")
else:
    print(s + ": BU KART NO GEÇERİ DEĞİLİDİR")

print("------------Son Digit------------")

sonuc, sonDigit = sonDigitDogrulama(s)
if sonuc == True:
    print(s + ": BU KART NO GEÇERLİDİR ")
else:
    print(s + ": BU KART NO GEÇERİ DEĞİLİDİR")

klasorAdi= os.path.dirname(sys.argv[0])
dosyaIsmi= klasorAdi + "/kartNo.txt"
if os.path.isfile(dosyaIsmi) ==True:
    dosya = open(dosyaIsmi, "r")
    i = 0 ;  j = 0
    for s in dosya:
        i += 1
        sonuc , cDigit = sonDigitDogrulama(s)
        if sonuc == True:
            if luhnAlgoritmasi(s)==True:
                j += 1
                s = s.rstrip()
                print("%5d : %5d : %1d : %s" % (i, j, cDigit, s))
    dosya.close()
else:
    print(dosyaIsmi + "Dosya diskte mevcut değil")