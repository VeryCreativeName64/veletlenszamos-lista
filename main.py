import feladatok
lista=[12, 21,56, 32, -5, -23, 35]

print("1. feladat")
db:int=feladatok.poz_szamok_szama(lista)
print(f"A pozitív számok száma {db}")

print("2. feladat")
db:int=feladatok.negativ_szamok_osszege(lista)
print(f"A negatív számok összege {db}")

print("3. feladat")
atlag:int=feladatok.ottel_oszthatok_atlaga(lista)
print(f"Az öttel oszthatók átlaga {atlag}")