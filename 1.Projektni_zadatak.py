
from datetime import date

korisnik={}

korisnik['ime']=input('Unesite ime korisnika:').capitalize()
korisnik['prezime']=input('Unesite prezime korisnika:').capitalize()
korisnik['telefon']=int(input('Unesite broj telefona:'))
korisnik['email']=input('Unesite email:').strip()

artikl={}

artikl['naslov']=input('Naslov artikla:')
artikl['opis']=input('Opis artikla:')
artikl['cijena']=float(input('Cijena artikla:'))

prodaja={}

dan=int(input('Unesite dan prodaje:'))
mjesec=int(input('Unesite mjesec prodaje:'))
godina=int(input('Unesite godinu prodaje:'))
prodaja['datum']=date(godina,mjesec,dan)

prodaja['korisnik']=korisnik
prodaja['artikl']=artikl

print('Informacije o artiklu:')
print(prodaja['artikl']['naslov'])
print(prodaja['artikl']['opis'])
print(prodaja['artikl']['cijena'])

print('Datum isteka prodaje:')
print('Dan:', prodaja['datum'].day)
print('Mjesec:', prodaja['datum'].month)
print('Godina', prodaja['datum'].year)

print('Informacije o korisniku:')
print(prodaja['korisnik']['ime'])
print(prodaja['korisnik']['prezime'])
print(prodaja['korisnik']['email'])




