from .projekt import Projekt
from utilities import unos_datuma, unos_cijelog_pozitivnog_broja

def unos_projekta(redni_broj):

    datum = unos_datuma('Unesite dan početka projekta: ')
    opis = input(f'Unesite opis {redni_broj} projekta: ')
    trosak = unos_cijelog_pozitivnog_broja(f'Unesite predviđeni trošak {redni_broj} projekta: ')

    return Projekt(datum, opis, trosak)