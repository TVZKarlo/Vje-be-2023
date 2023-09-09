from .komponenta import Komponenta
from utilities import unos_intervala

def unos_komponente(redni_broj):

    PN = input(f'Unesite Part Number {redni_broj}. komponente: ').capitalize()
    cijena= input(f'Unesite Part Number {redni_broj}. komponente: ').capitalize()
    print('Odaberite instrument:')
    print('\t1. nesto')
    print('\t2. Basprim')
    print('\t3. Harmonika')
    print('\t4. Bas')
    print('\t5. Bugarija')
    print('\t6. Bubanj')
    kategorija = unos_intervala(1, 6)

    return Komponenta(kategorija, PN, cijena)