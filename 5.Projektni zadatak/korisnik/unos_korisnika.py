from utilities import unos_telefona, unos_mail, unos_mail_m, unos_godina
from .korisnik import Korisnik

def unos_korisnika(redni_broj):
    ime = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    telefon = unos_telefona(f'Unesite telefon {redni_broj}. korisnika: ')
    email = unos_mail_m(f'Unesite email {redni_broj}. korisnika: ').strip()
    oib = input(f'Unesite OIB {redni_broj}. korisnika: ')
    prebivaliste = input(f'Unesite prebivaliste {redni_broj}. korisnika: ')
    broj = input(f'Unesite broj osobne iskaznice {redni_broj}. korisnika: ')

    return Korisnik(ime, prezime, telefon, email,)





