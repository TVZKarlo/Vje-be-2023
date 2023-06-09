def get_korisnik(redni_broj, korisnik):
    return f'\t {redni_broj}. Email: {korisnik.email}; Telefon: {korisnik.telefon}'


def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        print("Informacije o korisniku: ")
        korisnik.ispis()
