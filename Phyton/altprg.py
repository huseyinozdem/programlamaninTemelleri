
def yuvarlma(s):
    return round(s+0.0000000001)

def odevHesaplama(v):
    odev= 50+ v/2
    return odev
def ortHesapla(v , o , f):
    return v*0.3 + o *0.2 + f*0.5

vize = 60
odev = odevHesaplama(vize)
final = 45
print('Ödev :', odev)
print('Vize :', vize)

print('Final :', final)

ortalama = ortHesapla(vize,odev,final)
print('Ortalama :',ortalama)

print()
ortY = round(ortalama)
print('Yuvarlanmış Ortalama :', ortY)

ortY2 = yuvarlma(ortalama)

print()
print('Doğru Yuuvarlanmış Ortalama :', ortY2)

