import sys
import os
import random
klasorAdi = os.path.dirname(sys.argv[0])
dosyaIsmi = klasorAdi + "/test.txt"

soruSayisi = 40
ogrenciSayisi = 60
d = {}
dogruSayisi = {}
yalisSayisi = {}
bosSayisi = {}
puan = {}

def sinavHazirla():
  for j in range(1, soruSayisi + 1):
    r1 = random.randint(1, 5)
    d[0, j] = chr(64 + r1)

  for i in range(1, ogrenciSayisi + 1):
    for j in range(1, soruSayisi + 1):
      r1 = random.randint(1, 5)
      r2 = random.randint(0, 99)
      d[i, j] = chr(64 + r1)
      if r2 in range(41, 61):
        d[i, j] = chr(32)
      if r2 in range(61, 100):
        d[i, j] = d[0, j]



def sinavDegerlendir():
  for i in range(1, ogrenciSayisi + 1):
    dogruSayisi[i] = 0
    yalisSayisi[i] = 0
    bosSayisi[i] = 0
    puan[i] = 0

  soruBasinaDusenPuan = 100 / soruSayisi
  for i in range(1, ogrenciSayisi + 1):
    for j in range(1, soruSayisi + 1):
      if d[i, j] != chr(32):
        if d[i, j] == d[0, j]:
          dogruSayisi[i] += 1
        else:
          d[i, j] = chr(ord(d[i, j]) + 32)
          yalisSayisi[i] += 1
    bosSayisi[i] = soruSayisi - (dogruSayisi[i] + yalisSayisi[i])
    puan[i] = soruBasinaDusenPuan * dogruSayisi[i]


def sinavSirala():
  for i in range(1, ogrenciSayisi):
    for j in range(i + 1, ogrenciSayisi + 1):
      if puan[i] < puan[j]:
        for k in range(1, soruSayisi + 1):
          g = d[i, k]
          d[i, k] = d[j, k]
          d[j, k] = g

        g = dogruSayisi[i] ; dogruSayisi[i] = dogruSayisi[j] ; dogruSayisi[j] = g
        g = yalisSayisi[i] ; yalisSayisi[i] = yalisSayisi[j] ; yalisSayisi[j] = g
        g = bosSayisi[i] ; bosSayisi[i] = bosSayisi[j] ; bosSayisi[j] = g
        g = puan[i] ; puan[i] = puan[j] ; puan[j] = g

def sinavYaz():
  dosya = open(dosyaIsmi, "w")
  s = '    '
  for j in range(1, soruSayisi + 1):
    s += d[0 ,j]
  print(s, file=dosya)

  for i in range(1, ogrenciSayisi + 1):
    s = '%3d.' % i
    for j in range(1, soruSayisi + 1):
      s += d[i, j]

    s += ' ** Doğru Sayısı:%3d Yanlış Sayısı:%3d Boş Sayısı:%3d Puan:%6.2f' %\
         (dogruSayisi[i], yalisSayisi[i], bosSayisi[i], puan[i])
    print(s, file=dosya)
  dosya.close()

def sinavOku():
  if os.path.isfile(dosyaIsmi)==False:
    print("dosya diskte mevcut değil")
  else:
    dosya = open(dosyaIsmi, "r")
    for s in dosya:
      print(s, end="")

    dosya.close()


sinavHazirla()
sinavDegerlendir()
sinavSirala()
sinavYaz()
sinavOku()
