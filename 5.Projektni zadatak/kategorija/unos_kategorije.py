from artikl import unos_artikla
from utilities import unos_pozitivnog_cijelog_broja
from .kategorija import Kategorija

def unos_kategorije(redni_broj):
    naziv = input(f'Unesi naziv {redni_broj}. kategorije: ').capitalize()

    artikli = []
    br_artikala = unos_pozitivnog_cijelog_broja(f'Unesite broj artikala za {redni_broj}. kategoriju : ')
    for i in range(1, br_artikala+1):
        artikl = unos_artikla(i)
        artikli.append(artikl)

    return Kategorija(naziv, artikli)