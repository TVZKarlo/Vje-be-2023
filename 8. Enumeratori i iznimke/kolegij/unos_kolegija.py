from .kolegij import Kolegij


def unos_kolegija(redni_broj):
    ime = input(f'Unesite ime {redni_broj}. kolegija: ')
    ECTS = int(input(f'Unesite ECTS bodove za {redni_broj}. kolegij: '))

    return Kolegij(ime, ECTS)
