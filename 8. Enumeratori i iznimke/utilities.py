from iznimke import IznimkaPrazanTekst


def unos_intervala(min, max):
    running = True
    while running:
        try:
            broj = int(input(f'Unesite broj u intervalu {min}-{max}: '))

            if broj < min or broj > max:
                raise Exception(f'Morate upisati broj u intervalu {min}-{max}!')
        except ValueError:
            print('Morate upisati broj!')
        except Exception as e:
            print(e)
        else:
            return broj


def provjera_informacija(ime, prezime):
    try:
        if len(ime) == 0 or len(prezime) == 0:
            raise IznimkaPrazanTekst()

    except IznimkaPrazanTekst as e:
        return str(e)
    else:
        return None