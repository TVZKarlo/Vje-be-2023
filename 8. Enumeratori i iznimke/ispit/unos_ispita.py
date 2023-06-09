from datetime import date
from kolegij import get_kolegij
from utilities import unos_intervala
from .ispit import Ispit


def unos_ispita(kolegiji, redni_broj):
    print("Odaberite kolegij: ")
    for i, kolegij in enumerate(kolegiji, start=1):
        print('\t' + get_kolegij(i, kolegij))

    odabrani_kolegij = unos_intervala(1, len(kolegiji))

    kolegij = kolegiji[odabrani_kolegij-1]

    dan = int(input(f'Unesite dan {redni_broj}. ispita: '))
    mjesec = int(input(f'Unesite mjesec {redni_broj}. ispita: '))
    godina = int(input(f'Unesite godinu {redni_broj}. ispita: '))

    datum = date(godina, mjesec, dan)

    return Ispit(kolegij, datum)
