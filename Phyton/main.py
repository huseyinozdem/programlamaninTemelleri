import math

a = 1
b = 8
c = 7

if a == 0 :
    print("Bu bir İkinci Dereceden denklem değildir")
else:
    d = b * b - 4 * a * c
    if d < 0:
        print("Gerçel sayılarda kök yok.")
    if d == 0:
        cakisikkök = -b / 2 * a
        print("Çakışık iki kök vardır :", cakisikkök)
    if d > 0:
        birincikök = (-b - math.sqrt(d)) / 2 * a
        ikincikök = (-b + math.sqrt(d)) / 2 * a
        print("İki kök vardır")
        print("Birinci kök :", birincikök)
        print("İkinci kök :", ikincikök)