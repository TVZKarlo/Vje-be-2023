from datetime import date
from iznimke import IznimkaPrazanTekst, IznimkaTelefon


def unos_pozitivnog_cijelog_broja(poruka):

    while True:
        try:
            broj = int(input(f"{poruka}"))

            if broj < 0:
                raise Exception(f"Upisana vrojednost nije pozitivan cijeli broj!")

        except ValueError:
            print('Morate upisati cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_pozitivnog_realnog_broja(poruka):

    while True:
        try:
            broj = float(input(f"{poruka}"))

            if broj < 0:
                raise Exception(f"Upisana vrojednost nije pozitivan realni broj!")

        except ValueError:
            print('Morate upisati realan broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def unos_datuma(poruka):

    while True:
        try:
            dan = int(input(f"Unesite dan isteka prodaje: "))
            mjesec = int(input(f"Unesite mjesec isteka prodaje: "))
            godina = int(input(f"Unesite godinu isteka prodaje: "))

            datum = date(godina, mjesec, dan)

        except ValueError as e:
            print(e)

        else:
            return datum


def unos_intervala(min,max):

    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u intervalu {min}-{max}: "))

            if broj < min or broj > max:
                raise Exception(f"Broj nije u intervalu od {min} do {max}")

        except ValueError:
            print('Morate upisati broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def provjera_korisnickog_unosa(telefon, email, ime, prezime):
    try:
        if len(email) == 0 or len(ime) == 0 or len(prezime) == 0:
            raise IznimkaPrazanTekst()

        if len(telefon) != 8:
            raise IznimkaTelefon()

        broj = int(telefon)

    except IznimkaPrazanTekst as e:
        return str(e)

    except IznimkaTelefon as e:
        return str(e)

    except ValueError:
        return str('Telefon mora biti broj')

    else:
        return None


def provjera_unosa_artikla(naslov, opis, cijena, snaga):
    try:
        if len(naslov) == 0 or len(opis) == 0 or cijena == '' or snaga == '':
            raise IznimkaPrazanTekst()

        if int(cijena) < 0 or int(snaga) < 0:
            raise Exception(f"Potrebno upisati pozitivan cijeli broj!")

    except IznimkaPrazanTekst as e:
        return str(e)

    except ValueError:
        return('Potrebno upisati broj!')

    except Exception as e:
        return str(e)


def provjera_unosa_prodaje(korisnik, prodaja):
    try:
        if korisnik == '' or prodaja == '':
            raise IznimkaPrazanTekst()

    except IznimkaPrazanTekst as e:
        return str(e)
