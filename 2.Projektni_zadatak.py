
from datetime import date

#korisnik={}

#korisnik['ime']=input('Unesite ime korisnika:').capitalize()
#korisnik['prezime']=input('Unesite prezime korisnika:').capitalize()
#korisnik['telefon']=int(input('Unesite broj telefona:'))
#korisnik['email']=input('Unesite email:').strip()

#osobna_iskaznica={}

#osobna_iskaznica['broj']=int(input('Unesite broj:'))
#osobna_iskaznica['prebivalište']=input('Unesite prebivalište:')
#osobna_iskaznica['oib']=int(input('Unesite oib:'))

#korisnik['osobna_iskaznica']=osobna_iskaznica


#artikl={}

#artikl['naslov']=input('Naslov artikla:')
#artikl['opis']=input('Opis artikla:')
#artikl['cijena']=float(input('Cijena artikla:'))

#prodaja={}

#dan=int(input('Unesite dan prodaje:'))
#mjesec=int(input('Unesite mjesec prodaje:'))
#godina=int(input('Unesite godinu prodaje:'))
#prodaja['datum']=date(godina,mjesec,dan)

#prodaja['korisnik']=korisnik
#prodaja['artikl']=artikl
#prodaja['osobna_iskaznica']=osobna_iskaznica

#print('Informacije o artiklu:')
#print(prodaja['artikl']['naslov'])
#print(prodaja['artikl']['opis'])
#print(prodaja['artikl']['cijena'])

#print('Datum isteka prodaje:')
#print('Dan:', prodaja['datum'].day)
#print('Mjesec:', prodaja['datum'].month)
#print('Godina', prodaja['datum'].year)

#print('Informacije o korisniku:')
#print(prodaja['korisnik']['ime'])
#print(prodaja['korisnik']['prezime'])
#print(prodaja['korisnik']['email'])


#print('Broj:',prodaja['korisnik'],osobna_iskaznica['broj'])
#print('Prebivalište:',prodaja['korisnik'],osobna_iskaznica['prebivalište'])
#print('OIB:',prodaja['korisnik'],osobna_iskaznica['oib'])

##########################################################################################

korisnici = []
kategorije = []
prodaje = []

broj_vozacki = int(input('Unesite broj vozačkih: '))
vozacke = []

for i in range(1, broj_vozacki + 1):
    vozacka = {}
    vozacka['klasa_vozacke'] = input(f'Unesite klasu {i}. vozacke dozvole: ')
    dan = int(input(f"Unesite dan izdavanja {i}. vozacke dozvole: "))
    mjesec = int(input(f"Unesite mjesec izdavanja {i}. vozacke dozvole: "))
    godina = int(input(f"Unesite godinu izdavanja {i}. vozacke dozvole: "))
    vozacka['datum'] = date(godina, mjesec, dan)
    vozacke.append(vozacka)

broj_korisnika = int(input("Unesite broj korisnika: "))

for i in range(1, broj_korisnika + 1):
    korisnik = {}
    korisnik['Ime'] = input(f"Unesite ime {i}. korisnika: ").capitalize()
    korisnik['Prezime'] = input(f"Unesite prezime {i}. korisnika: ").capitalize()
    korisnik['Telefon'] = int(input(f"Unesite telefon {i}. korisnika: "))
    korisnik['Email'] = input(f"Unesite email {i}. korisnika: ").strip()

    for j, vozacka in enumerate(vozacke, start=1):
        print(f"\t{j}. {vozacka['klasa_vozacke']}, {vozacka['datum']}")

    odabrana_vozacka=int(input("Odaberite vozacku dozvolu: "))
    korisnik['vozacka']=vozacke[odabrana_vozacka -1]
    korisnici.append(korisnik)


broj_kategorija = int(input("Unesite broj kategorija: "))

for i in range(1, broj_kategorija + 1):
    kategorija = {}
    artikli = []

    kategorija["Naziv"] = input(f"Unesite naziv {i}. kategorije: ")

    broj_artikala = int(input(f"Unesite broj artikala za {i}. kategoriju: "))
    for j in range(1, broj_artikala + 1):
        artikl = {}
        artikl["Naslov"] = input(f"Unesite naslov {j}. artikla: ")
        artikl["Opis"] = input(f"Unesite opis {j}. artikla: ")
        artikl["Cijena"] = float(input(f"Unesite cijenu {j}. artikla: "))
        artikli.append(artikl)

    kategorija["Artikli"] = artikli
    kategorije.append(kategorija)


broj_prodaja = int(input("Unesite broj prodaja: "))

for i in range(1, broj_prodaja + 1):
    prodaja = {}

    dan = int(input(f"Unesite dan isteka {i}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {i}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {i}. prodaje: "))
    prodaja["Datum"] = date(godina, mjesec, dan)

#Odabir korisnika
    print(f"Odaberite korisnika {i}. prodaje: ")
    for j, korisnik in enumerate(korisnici, start=1):
        print(f'\t{j}. {korisnik["Ime"]} {korisnik["Prezime"]}')

    odabrani_korisnik = int(input("Odabrani korisnik: "))

#Odabir kategorije
    print(f"Odaberite kategoriju {i}. prodaje: ")
    for j, kategorija in enumerate(kategorije, start=1):
        print(f'\t{j}. {kategorija["Naziv"]}')

    odabrana_kategorija = int(input("Odabrana kategorija: "))

#Odabir artikla
    print(f"Odaberite artikl {i}. prodaje: ")

    for j, artikl in enumerate(kategorije[odabrana_kategorija-1]["Artikli"], start=1):
        print(f'\t{j}. {kategorije[odabrana_kategorija-1]["Artikli"][j-1]["Naslov"]}')

    odabrani_artikl = int(input("Odabrani artikl: "))

    prodaja['Korisnik'] = korisnici[odabrani_korisnik - 1]
    prodaja["Artikl"] = kategorije[odabrana_kategorija - 1]["Artikli"][odabrani_artikl - 1]
    prodaje.append(prodaja)


for i, prodaje in enumerate(prodaje, start=1):
    print(f"Prodaja {i}: ")
    print('Informacije o korisniku: ')
    print(f"\tIme: {prodaje['Korisnik']['Ime']}")
    print(f"\tPrezime: {prodaje['Korisnik']['Prezime']}")
    print(f"\tTelefon: {prodaje['Korisnik']['Telefon']}")
    print(f"\tEmail: {prodaje['Korisnik']['Email']}")
    print(f"\tVozačka: {prodaje['Korisnik']['vozacka']['klasa_vozacke']} {prodaje['Korisnik']['vozacka']['datum']}")

    print('Informacije o artiklu: ')
    print(f'\t Naslov: {prodaje["Artikl"]["Naslov"]}')
    print(f'\t Opis: {prodaje["Artikl"]["Opis"]}')
    print(f'\t Cijena: {prodaje["Artikl"]["Cijena"]}')

    print('Datum isteka prodaje: ')
    print(f'\t Dan: {prodaje["Datum"].day}')
    print(f'\t Mjesec: {prodaje["Datum"].month}')
    print(f'\t Godina: {prodaje["Datum"].year}')


