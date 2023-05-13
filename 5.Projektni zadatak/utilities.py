from datetime import date


def unos_pozitivnog_cijelog_broja(poruka):
    while True:
        try:
            broj = int(input(poruka))

            if broj < 0:
                raise Exception('Unesite poziticni cijeli broj!')

        except ValueError:
            print('Unesli ste slovo umjesto broja!')
        except Exception as e:
            print(e)
        else:
            return broj


def unos_pozitivnog_realnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati realni broj!')

        except ValueError:
            print('Unesli ste znak a ne realni broj.')
        except Exception as e:
            print(e)
        else:
            return broj


def unos_datuma(poruka):
    while True:
            try:
                dan = int(input(poruka))
                mjesec = int(input(f'Unesite mjesec isteka prodaje: '))
                godina = int(input(f'Unesite godinu isteka prodaje: '))
                datum = date(godina, mjesec, dan)

            except ValueError as e:
                print(e)
            else:
                return datum


def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj<min or broj>max:
                raise Exception(f"Unesite broj unutar intervala {min}-{max}.")

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj


def unos_telefona(poruka):
    while True:
        try:
            broj = unos_pozitivnog_cijelog_broja(poruka)

            if len(str(broj)) !=8:
                raise Exception(f'Uneseni broj mora imat 8 znamenaka!')

        except Exception as e:
            print(e)

        else:
            return broj



def unos_mail(poruka):
    while True:
        try:
            mail = input(poruka)

            while '@' not in mail:
                raise Exception(f'Uneseni mail mora imati znak @!')

        except Exception as e:
            print(e)

        else:
            return mail


def unos_mail_m(poruka):
    while True:
        try:
            email = input(poruka)
            index = email.index('@')

        except ValueError:
            print('Uneseni mail mora sadržavati znak @!')

        else:
            return email


def unos_godina(poruka):
    while True:
        try:
            godine = unos_pozitivnog_cijelog_broja(poruka)

            if godine < 18 or godine > 120:
                raise Exception(f'Broj godina mora biti iznad 18 i ispod 120!')

        except Exception as e:
            print(e)
        else:
            return godine


