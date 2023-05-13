from datetime import date

# inicijalizacija praznih listi za korisnike, kategorije, prodaju i telefone
korisnici = []
kategorije = []
prodaje = []
telefoni = []

# unos brojeva telefona
br_telefona = int(input('Unesi željeni broj telefona: '))
for i in range(1, br_telefona + 1):
    telefon = {}
    telefon['pozivni_broj'] = int(input('Unesi pozivni broj: '))
    telefon['broj'] = int(input('Unesi broj telefona: '))
    telefon['proizvodac'] = input('Unesi proizvođača telefona: ')
    telefoni.append(telefon)

# unos korisnika
br_korisnika = int(input("Unesite broj korisnika: "))
for i in range(1, br_korisnika + 1):
    korisnik = {}
    korisnik['ime'] = input(f'Unesite ime {i}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {i}. korisnika: ').capitalize()
#   korisnik['tel'] = int(input(f'Unesite broj telefona {i}. korisnika: '))
    korisnik['email'] = input(f'Unesite email {i}. korisnika: ').strip()
    korisnici.append(korisnik)

    print(f'Odaberite broj telefona za korisnika {i}. prodaje: ')
    for j, telefon in enumerate(telefoni, start=1):
        print(f"{j}. {telefon['broj']} ")

    odabrani_telefon = int(input('Odabrani telefon: '))
    korisnik['tel'] = telefoni[odabrani_telefon-1]

# unos kategorija i artikala
br_kategorija = int(input("Unesite broj kategorija: "))
for i in range(1, br_kategorija + 1):
    kategorija = {}
    kategorija['naziv'] = input(f'Unesi naziv {i}. kategorije: ').capitalize()

    artikli = []
    br_artikala = int(input(f'Unesite broj artikala za {i}. kategoriju : '))
    for j in range(1, br_artikala + 1):
        artikl = {}
        artikl['naslov'] = input(f'Unesite naslov {j}. artikla: ').capitalize()
        artikl['opis'] = input(f'Unesite opis {j}. artikla: ').capitalize()
        artikl['cijena'] = float(input(f'Unesite cijenu {j}. artikla: '))
        artikli.append(artikl)

    kategorija['artikli'] = artikli
    kategorije.append(kategorija)

br_prodaja = int(input('Unesi željeni broj prodaja: '))
for i in range(1, br_prodaja + 1):
    prodaja = {}
    dan = int(input(f'Unesite dan isteka {i}. prodaje: '))
    mjesec = int(input(f'Unesite mjesec {i}. prodaje: '))
    godina = int(input(f'Unesite godinu {i}. prodaje: '))
    prodaja['datum'] = date(godina, mjesec, dan)

    print(f'Odaberite korisnika {i}. prodaje: ')
    for j, korisnik in enumerate(korisnici, start=1):
        print(f"{j}. {korisnik['ime']} {korisnik['prezime']}")

    odabrani_korisnik = int(input('Odabrani korisnik: '))

    print(f'Odaberite kategoriju {i}. prodaje: ')
    for k, kategorija in enumerate(kategorije, start=1):
        print(f"{k}. {kategorija['naziv']}")

    odabrana_kategorija = int(input('Odabrana kategorija: '))

    print(f'Odaberite artikl {i}. prodaje: ')
    for n, artikl in enumerate(kategorije[odabrana_kategorija-1]['artikli'], start=1):
        print(f"{n}. {kategorije[odabrana_kategorija-1]['artikli'][n-1]['naslov']}")

    odabrani_artikl = int(input('Odabrani artikl: '))

    prodaja['korisnik'] = korisnici[odabrani_korisnik-1]
    prodaja['artikl'] = kategorije[odabrana_kategorija-1]['artikli'][odabrani_artikl-1]
    prodaje.append(prodaja)

for i, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}: ")
    print('Informacije o korisniku: ')
    print(f'\t Ime: {prodaja["korisnik"]["ime"]}')
    print(f'\t Prezime: {prodaja["korisnik"]["prezime"]}')
    print(f'\t Telefon: {prodaja["korisnik"]["tel"]["broj"]}')
    print(f'\t Email: {prodaja["korisnik"]["email"]}')

    print('Informacije o artiklu: ')
    print(f'\t Naslov: {prodaja["artikl"]["naslov"]}')
    print(f'\t Opis: {prodaja["artikl"]["opis"]}')
    print(f'\t Cijena: {prodaja["artikl"]["cijena"]}')

    print('Datum isteka prodaje: ')
    print(f'\t Dan: {prodaja["datum"].day}')
    print(f'\t Mjesec: {prodaja["datum"].month}')
    print(f'\t Godina: {prodaja["datum"].year}')

    print('-'*40)
