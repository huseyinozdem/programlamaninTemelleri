import math

a = float(input("a kat sayısı :"))
b = float(input("b kat sayısı :"))
c = float(input("c kat sayısı :"))

if a == 0:
    print("Bu bir İkinci Dereceden denklem değildir")
else:
    d = b * b - 4 * a * c
    if d < 0:
        print("Gerçel sayılarda kök yok.")
    if d == 0:
        cakisikkok = -b / (2 * a)
        print("Çakışık iki kök vardır :", cakisikkok)
    if d > 0:
        birincikok = (-b - math.sqrt(d)) / (2 * a)
        ikincikok = (-b + math.sqrt(d)) / (2 * a)
        print("İki kök vardır")
        print("Birinci kök :", birincikok)
        print("İkinci kök :", ikincikok)
