def ispis_artikla(artikl):
    print(f"\tartikl {artikl['Naslov']['Opis']['Cijena']}")

def get_artikl(redni_broj,artikl):
    return f"\t{redni_broj}. {artikl['Naslov']}"