
from datetime import date

korisnik={}

korisnik['ime']=input('Unesite ime korisnika:').capitalize()
korisnik['prezime']=input('Unesite prezime korisnika:').capitalize()
korisnik['telefon']=int(input('Unesite broj telefona:'))
korisnik['email']=input('Unesite email:').strip()

vozačka={}

vozačka['klasa_vozila']=input('Unesite klasu vozila:')

dan=int(input('Unesite dan prodaje:'))
mjesec=int(input('Unesite mjesec prodaje:'))
godina=int(input('Unesite godinu prodaje:'))
vozačka['datum']=date(godina,mjesec,dan)

korisnik['vozačka']=vozačka

# artikl={}
#
# artikl['naslov']=input('Naslov artikla:')
# artikl['opis']=input('Opis artikla:')
# artikl['cijena']=float(input('Cijena artikla:'))
#
prodaja={}

dan=int(input('Unesite dan izdavanja:'))
mjesec=int(input('Unesite mjesec izdavanja:'))
godina=int(input('Unesite godinu izdavanja:'))

# prodaja['datum']=date(godina,mjesec,dan)
prodaja['korisnik']=korisnik
# prodaja['artikl']=artikl

# print('Informacije o artiklu:')
# print(prodaja['artikl']['naslov'])
# print(prodaja['artikl']['opis'])
# print(prodaja['artikl']['cijena'])

# print('Datum isteka prodaje:')
# print('Dan:', prodaja['datum'].day)
# print('Mjesec:', prodaja['datum'].month)
# print('Godina', prodaja['datum'].year)

# print('Informacije o korisniku:')
# print(prodaja['korisnik']['ime'])
# print(prodaja['korisnik']['prezime'])
# print(prodaja['korisnik']['email'])


print('Klasa vozila:',prodaja['korisnik']['vozačka']['klasa_vozila'])
print('Datum:',prodaja['korisnik']['vozačka']['datum'])




##########################################################################################
#
# korisnici = []
# kategorije = []
# prodaje = []
#
# broj_korisnika = int(input("Unesite broj korisnika: "))
#
# for i in range(1, broj_korisnika + 1):
#     korisnik = {}
#     korisnik["Ime"] = input(f"Unesite ime {i}. korisnika: ").capitalize()
#     korisnik["Prezime"] = input(f"Unesite prezime {i}. korisnika: ").capitalize()
#     korisnik["Telefon"] = int(input(f"Unesite telefon {i}. korisnika: "))
#     korisnik["Email"] = input(f"Unesite email {i}. korisnika: ").strip()
#     korisnici.append(korisnik)
#
#
# broj_kategorija = int(input("Unesite broj kategorija: "))
#
# for i in range(1, broj_kategorija + 1):
#     kategorija = {}
#     artikli = []
#
#     kategorija["Naziv"] = input(f"Unesite naziv {i}. kategorije: ")
#
#     broj_artikala = int(input(f"Unesite broj artikala za {i}. kategoriju: "))
#     for j in range(1, broj_artikala + 1):
#         artikl = {}
#         artikl["Naslov"] = input(f"Unesite naslov {j}. artikla: ")
#         artikl["Opis"] = input(f"Unesite opis {j}. artikla: ")
#         artikl["Cijena"] = float(input(f"Unesite cijenu {j}. artikla: "))
#         artikli.append(artikl)
#
#     kategorija["Artikli"] = artikli
#     kategorije.append(kategorija)
#
#
# broj_prodaja = int(input("Unesite broj prodaja: "))
#
# for i in range(1, broj_prodaja + 1):
#     prodaja = {}
#
#     dan = int(input(f"Unesite dan isteka {i}. prodaje: "))
#     mjesec = int(input(f"Unesite mjesec isteka {i}. prodaje: "))
#     godina = int(input(f"Unesite godinu isteka {i}. prodaje: "))
#     prodaja["Datum"] = date(godina, mjesec, dan)
#
# #Odabir korisnika
#     print(f"Odaberite korisnika {i}. prodaje: ")
#     for j, korisnik in enumerate(korisnici, start=1):
#         print(f'\t{j}. {korisnik["Ime"]} {korisnik["Prezime"]}')
#
#     odabrani_korisnik = int(input("Odabrani korisnik: "))
#
# #Odabir kategorije
#     print(f"Odaberite kategoriju {i}. prodaje: ")
#     for j, kategorija in enumerate(kategorije, start=1):
#         print(f'\t{j}. {kategorija["Naziv"]}')
#
#     odabrana_kategorija = int(input("Odabrana kategorija: "))
#
# #Odabir artikla
#     print(f"Odaberite artikl {i}. prodaje: ")
#
#     for j, artikl in enumerate(kategorije[odabrana_kategorija-1]["Artikli"], start=1):
#         print(f'\t{j}. {kategorije[odabrana_kategorija-1]["Artikli"][j-1]["Naslov"]}')
#
#     odabrani_artikl = int(input("Odabrani artikl: "))
#
#     prodaja["Korisnik"] = korisnici[odabrani_korisnik - 1]
#     prodaja["Artikl"] = kategorije[odabrana_kategorija - 1]["Artikli"][odabrani_artikl - 1]
#     prodaje.append(prodaja)
#
#
# for i, prodaja in enumerate(prodaje, start=1):
#     print(f"Prodaja {i}: ")
#     print('Informacije o korisniku: ')
#     print(f'\tIme: {prodaja["Korisnik"]["Ime"]}')
#     print(f'\tPrezime: {prodaja["Korisnik"]["Prezime"]}')
#     print(f'\tTelefon: {prodaja["Korisnik"]["Telefon"]}')
#     print(f'\tEmail: {prodaja["Korisnik"]["Email"]}')
#
#     print('Informacije o artiklu: ')
#     print(f'\t Naslov: {prodaja["Artikl"]["Naslov"]}')
#     print(f'\t Opis: {prodaja["Artikl"]["Opis"]}')
#     print(f'\t Cijena: {prodaja["Artikl"]["Cijena"]}')
#
#     print('Datum isteka prodaje: ')
#     print(f'\t Dan: {prodaja["Datum"].day}')
#     print(f'\t Mjesec: {prodaja["Datum"].month}')
#     print(f'\t Godina: {prodaja["Datum"].year}')


