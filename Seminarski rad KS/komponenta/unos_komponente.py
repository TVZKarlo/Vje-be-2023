from .komponenta import Komponenta
from utilities import unos_intervala

def unos_komponente(redni_broj):

    PN = input(f'Unesite Part Number {redni_broj}. komponente: ').capitalize()
    cijena= input(f'Unesite cijenu {redni_broj}. komponente: ').capitalize()
    print('Odaberite kategoriju:')
    print('\t1. IC')
    print('\t2. Tranzistor')
    print('\t3. Reley')
    print('\t4. Otpornik')
    print('\t5. Kondenzator')
    print('\t6. Zavojnica')
    kategorija = unos_intervala(1, 6)

    return Komponenta(kategorija, PN, cijena)