from ispit import get_ispit
from utilities import unos_intervala
from .vanredni_student import VanredniStudent
from .redovni_student import RedovniStudent


def unos_studenta(ispiti, redni_broj):
    ime = input(f"Unesite ime {redni_broj}. studenta: ")
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ")

    print("Odaberite ispit: ")
    for i, ispit in enumerate(ispiti, start=1):
        print(f"\t" + get_ispit(ispit, i))

    odabrani_ispit = unos_intervala(1, len(ispiti))

    ispit = ispiti[odabrani_ispit - 1]

    print("Odaberite tip studenta: ")
    print("\t1.Redovni")
    print("\t2.Vanredni")
    tip_studenta = int(input("Unesite tip studenta: "))

    if tip_studenta == 1:
        broj_prijava = input("Unesite broj prijava na ispit: ")

        return RedovniStudent(ime, prezime, ispit, broj_prijava)
    else:
        return VanredniStudent(ime, prezime, ispit)