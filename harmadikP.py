import math

'''
Írj programot, mely beolvas két 
pozitív egész számot, és kiírja a 
zámtani és mértani közepüket! A 
gyökvonáshoz használd a Math.Sqrt() 
függvényt!

elsoSzam = input('Kérek egy számot: ')
masodikSzam = input('Kérek egy másik számot:') 

esz, msz = int(elsoSzam), int(masodikSzam)

szamtaniKozep = (esz + msz) / 2
mertaniKozep = math.sqrt(esz * msz)

print('A két szám: {}, {} számtani közepe: {:.3f}, mértani közepe: {:.3f}'.format(esz, msz, szamtaniKozep, mertaniKozep))
'''
'''
2.Feladat: Írj programot, ami beolvassa a másodfokú egyenlet együtthatóit, 
és kiírja az egyenlet megoldásait, ha vannak! 

elso = input('Kérem a-értékét: ')
masodik = input('Kérem b-értékét: ')
harmadik = input('Kérem c-értékét: ')

a, b, c = int(elso), int(masodik), int(harmadik)

diszk = b * b - 4 * a * c

if diszk < 0:
	print('Nincs valós megoldás.')
elif diszk > 0:
	elsoMegoldas = (-b + math.sqrt(diszk)) / (2 * a)
	masodikMegoldas = (-b - math.sqrt(diszk)) / (2 * a)
	print('Első megoldás: {}, második megoldás: {}'.format(elsoMegoldas, masodikMegoldas))
else:
	megoldas = -b / (2 * a)
	print('Az egyetlen megoldás. {}'.format(megoldas))
'''
'''
3.Feladat: Írj programot, mely beolvas egy pozitív egész számot, és 
kiírja az egész számokat a képernyőre eddig a számig, egymástól szóközzel 
elválasztva!

bevitel = input('Kérek egy számot: ')
szam = int(bevitel)

szoveg = '0'
i = 1

while i < (szam + 1):
	szoveg += ' ' + str(i)
	i += 1

# for x in range(1, szam + 1):
#	szoveg += ' ' + str(x)

print(szoveg)
'''
'''
4.feladat: Írj programot, mely beolvas egy pozitív egész számot, és kiírja 
az osztóit, valamint az osztóinak az összegét!

bevitel = input('Kérek egy számot: ')
szam = int(bevitel)
print('A szám: {} - osztói:'.format(szam))

# for x in range(1, szam + 1):
#	if szam % x == 0:
#		print(x)

i = 1
osszeg = 0

while i < szam + 1:
	kiir = 'i = {}, '.format(i)
	if szam % i == 0:
		osszeg += i
		kiir += 'osszeg = {}, {}-osztója a számnak: {}'.format(osszeg, i, szam)
	else:
		kiir += 'osszeg = {}'.format(osszeg)
	print(kiir)
	i += 1
'''
'''
5.Feladat: Írj programot, mely beolvas egy pozitív egész számot, és megmondja,
hogy tökéletes szám-e! (A tökéletes számok azok, melyek osztóinak összege 
egyenlő a szám kétszeresével. Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.)
'''
bevitel = input('Kérek egy számot: ')
szam = int(bevitel)

i = 1
osszeg = 0

while i < szam + 1:
	if szam % i == 0:
		osszeg += i
	i += 1

if osszeg == 2 * szam:
	print('A szám: {} tökéletes.'.format(szam))
else:
	print('A szám: {} nem tökéletes.'.format(szam))

	
