from utilities import unos_pozitivnog_realnog_broja, unos_pozitivnog_cijelog_broja, unos_intervala
from .stan import Stan
from .automobil import Automobil


def unos_artikla(redni_broj):
    naslov = input(f"Unesite naslov {redni_broj}. artikla: ")
    opis = input(f"Unesite opis {redni_broj}. artikla: ")
    cijena = unos_pozitivnog_realnog_broja(f"Unesite cijenu {redni_broj}. artikla: ")

    print('Tipovu artikla: ')
    print('1. Stan')
    print('2. Automobil')

    tip_artikla = unos_intervala(1, 2)

    if tip_artikla == 1:
        kvadratura = unos_pozitivnog_cijelog_broja(f'Unesite kvadraturu stana: ')

        return Stan(naslov, opis, cijena, kvadratura)

    elif tip_artikla == 2:
        snaga = unos_pozitivnog_cijelog_broja(f'Unesite snagu automobila: ')

        return Automobil(naslov, opis, cijena, snaga)
