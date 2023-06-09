def get_ispit(ispit, redni_broj):
    return f"{redni_broj}. Ispit iz kolegija {ispit.kolegij.ime}"


def ispis_svih_ispita(ispiti):
    print('Popis svih ispita: ')
    for ispit in ispiti:
        ispit.ispis()