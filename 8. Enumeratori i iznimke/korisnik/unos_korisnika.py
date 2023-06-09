from utilities import unos_pozitivnog_cijelog_broja, unos_intervala
from .privatni_korisnik import PrivatniKorisnik
from .poslovni_korisnik import PoslovniKorisnik


def unos_korisnika(redni_broj):
    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika: ")
    email = input(f"Unesite email {redni_broj}. korisnika: ").strip()

    print('Odaberite tip korisnika: ')
    print('\t1. Poslovni korisnik')
    print('\t2. Privatni korisnik')
    tip_korisnika = unos_intervala(1, 2)

    if tip_korisnika == 1:
        naziv = input(f"Unesite naziv {redni_broj}. korisnika: ").capitalize()
        web = input(f"Unesite web {redni_broj}. korisnika: ")

        return PoslovniKorisnik(naziv, web, telefon, email)


    elif tip_korisnika == 2:
        ime = input(f"Unesite ime {redni_broj}. korisnika: ").capitalize()
        prezime = input(f"Unesite prezime {redni_broj}. korisnika: ").capitalize()

        return PrivatniKorisnik(ime, prezime, telefon, email)
