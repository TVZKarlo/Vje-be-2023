from artikl import unos_artikla
def unos_kategorije(redni_broj):
    kategorija = {}
    kategorija['naziv'] = input(f'Unesite naziv {redni_broj}. kategorije: ')
    kategorija['artikli'] = []

    br_artikala = int(input(f'Unesite broj artikala za {redni_broj}. kategoriju: '))
    for i in range(1, br_artikala + 1):
        artikl=unos_artikla(i)
        kategorija['artikli'].append(artikl)

    return kategorija