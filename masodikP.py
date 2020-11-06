'''
1.Feladat: Írj programot, beolvassa 
a felhasználó nevét, 
majd köszön neki!

nev = input('Kérek egy nevet: ')
print('A felhasználó neve: {}'.format(nev))
'''
'''
2.Feladat: Írj programot, ami beolvas egy számot, 
majd kiírja a kétszeresét!

szam = input('Kérek egy számot: ')
kiir = 'A szám: {} kétszerese: {}'.format(szam, 2 * int(szam))
print(kiir)
'''
'''
3.Feladat: Írj programot, ami beolvas két számot, majd kiírja:
a. az összegüket;
b. különbségüket;
c. szorzatukat;
d. hányadosukat, ha lehet!

elsoSzam = input('Kérek egy számot: ')
masodikSzam = input('Kérek egy másik számot: ')

esz, msz = int(elsoSzam), int(masodikSzam)

osszeg = esz + msz
kulonbseg = esz - msz
szorzat = esz * msz
hanyados = esz / msz

kiirOsszeg = 'A számok: {}, {} összege: {}'.format(esz, msz, osszeg)
print(kiirOsszeg)
kiirKulonbseg = 'A számok: {}, {} különbsége: {}'.format(esz, msz, kulonbseg)
print(kiirKulonbseg)
kiirSzorzat = 'A számok: {}, {} szorzata: {}'.format(esz, msz, szorzat)
print(kiirSzorzat)
kiirHanyados = 'A számok: {}, {} hányadosa: {:.3f}'.format(esz, msz, hanyados)
print(kiirHanyados)
'''
'''
4.Feladat: Írj programot, mely beolvas két egész számot, és 
kiírja a képernyőre a nagyobbikat!

elsoSzam = input('Kérek egy számot: ')
masodikSzam = input('Kérek egy másik számot: ')

esz, msz = int(elsoSzam), int(masodikSzam)

if esz > msz: 
	print('A nagyobbik szám: {}'.format(esz))
elif msz > esz:
	print('A nagyobbik szám: {}'.format(msz))
else:
	print('A két szám egyenlő.')
'''
'''
5.Feladat: Írj programot, mely beolvas három egész számot, és kiírja a 
képernyőre a legkisebbet!

elsoSzam = input('Kérek egy számot: ')
masodikSzam = input('Kérek egy másik számot: ')
harmadikSzam = input('Kérek egy harmadik számot: ')

esz, msz, hsz = int(elsoSzam), int(masodikSzam), int(harmadikSzam)

if esz < msz:
	if esz <= hsz:
		print('A legkisebb szám: {}'.format(esz))
	else:
		print('A legkisebb szám: {}'.format(hsz))
else:
	if msz <= hsz:
		print('A legkisebb szám: {}'.format(msz))
	else:
		print('A legkisebb szám: {}'.format(hsz))
'''
'''
6.Feladat: Írj programot, ami beolvassa a háromszög oldalainak 
hosszát, és megmondja, hogy ilyen oldalakkal szerkeszthető-e 
háromszög!
'''
elsoSzam = input('Kérek egy számot: ')
masodikSzam = input('Kérek egy másik számot: ')
harmadikSzam = input('Kérek egy harmadik számot: ')

esz, msz, hsz = int(elsoSzam), int(masodikSzam), int(harmadikSzam)

kifejezes = esz + msz > hsz and esz + hsz > msz and msz + hsz > esz

if kifejezes:
	print('A három oldalból {}, {}, {} háromszög szerkeszthető'.format(esz, msz, hsz))
else:
	print('A három oldalból {}, {}, {} háromszög nem szerkeszthető'.format(esz, msz, hsz))

