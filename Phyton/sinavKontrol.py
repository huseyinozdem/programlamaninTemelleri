import random
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
  for j in range(1, soruSayisi + 1):
    print(d[0, j], end="")
  print()
  for i in range(1, ogrenciSayisi + 1):
    for j in range(1, soruSayisi + 1):
      print(d[i, j], end="")
    print()






sinavHazirla()
sinavDegerlendir()

