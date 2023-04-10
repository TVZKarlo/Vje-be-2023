def ispis_korisnika(korisnik):

#ispisuje sve podatke o korisniku
    print(f"\tKorisnik {korisnik['ime']['prezime']['telefon']['email']}")

def get_korisnik(redni_broj, korisnik):
    return f"\t{redni_broj}. {korisnik['ime']['prezime']}"