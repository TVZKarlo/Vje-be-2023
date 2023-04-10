
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
#
korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input("Unesite broj korisnika: "))

for i in range(1, broj_korisnika + 1):
    korisnik = {}
    korisnik["Ime"] = input(f"Unesite ime {i}. korisnika: ").capitalize()
    korisnik["Prezime"] = input(f"Unesite prezime {i}. korisnika: ").capitalize()
    korisnik["Telefon"] = int(input(f"Unesite telefon {i}. korisnika: "))
    korisnik["Email"] = input(f"Unesite email {i}. korisnika: ").strip()
    korisnici.append(korisnik)                                                             #pospremanje u listu korisnici

#TODO slično kao prodaja

broj_osobnih_iskaznica=int(input('Unesite broj osobnih iskaznica:'))
osobne_iskaznice=[]

for i in range(1, broj_osobnih_iskaznica +1 ):
    osobna_iskaznica={}
    osobna_iskaznica['broj']=int(input(f'Unesite broj {i}. iskaznice:'))
    osobna_iskaznica['prebivalište'] = input(f'Unesite {i}. prebivalište:')
    osobna_iskaznica['oib'] = int(input(f'Unesite broj {i}. oib-a:'))
    osobne_iskaznice.append(osobna_iskaznica)

    for j, osobna_iskaznica in enumerate(osobne_iskaznice, start=1):
        print(f"\t{j}. {osobna_iskaznica['broj']}")

    odabrana_osobna_iskaznica=int(input('Odaberite osobunu iskaznicu: '))-1
    korisnik['osobna_iskaznica']=osobne_iskaznice[odabrana_osobna_iskaznica]
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

for i in range(1, broj_prodaja + 1):                                    #pogledati za zadatak
    prodaja = {}

    dan = int(input(f"Unesite dan isteka {i}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {i}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {i}. prodaje: "))
    prodaja["Datum"] = date(godina, mjesec, dan)

#Odabir korisnika
    print(f"Odaberite korisnika {i}. prodaje: ")
    for j, korisnik in enumerate(korisnici, start=1):                   #enumarate brojač u for petlji
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

    prodaja["Korisnik"] = korisnici[odabrani_korisnik - 1]
    prodaja["Artikl"] = kategorije[odabrana_kategorija - 1]["Artikli"][odabrani_artikl - 1]
    prodaja['ososbna_iskaznica']=korisnici[odabrana_osobna_iskaznica-1]
    prodaje.append(prodaja)


for i, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}: ")
    print('Informacije o korisniku: ')
    print(f'\tIme: {prodaja["Korisnik"]["Ime"]}')
    print(f'\tPrezime: {prodaja["Korisnik"]["Prezime"]}')
    print(f'\tTelefon: {prodaja["Korisnik"]["Telefon"]}')
    print(f'\tEmail: {prodaja["Korisnik"]["Email"]}')
    print(f'\tBroj osobne iskaznice: {prodaja["Korisnik"]["osobna_iskaznica"]["broj"]}')


    print('Informacije o artiklu: ')
    print(f'\t Naslov: {prodaja["Artikl"]["Naslov"]}')
    print(f'\t Opis: {prodaja["Artikl"]["Opis"]}')
    print(f'\t Cijena: {prodaja["Artikl"]["Cijena"]}')

    print('Datum isteka prodaje: ')
    print(f'\t Dan: {prodaja["Datum"].day}')
    print(f'\t Mjesec: {prodaja["Datum"].month}')
    print(f'\t Godina: {prodaja["Datum"].year}')










# #Odabir kategorije
# print(f"Odaberite iskaznicu {i}. : ")
# for i, osobna_iskaznice in enumerate(osobne_iskaznice, start=1):
# print(f'\t{i}. {prodaja["korisnik"]["osobna_iskaznica"][i-1]["broj"]}')