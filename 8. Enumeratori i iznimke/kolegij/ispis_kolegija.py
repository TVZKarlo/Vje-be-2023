def get_kolegij(redni_broj, kolegij):
    return f"{redni_broj}. {kolegij.ime}"


def ispis_svih_kolegija(kolegiji):
    print('Popis svih kolegija: ')
    for kolegij in kolegiji:
        kolegij.ispis()