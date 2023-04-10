def unos_artikla(redni_broj):

    artikl = {}
    artikl["Naslov"] = input(f"Unesite naslov artikla: ")
    artikl["Opis"] = input(f"Unesite opis artikla: ")
    artikl["Cijena"] = float(input(f"Unesite cijenu artikla: "))

    return artikl
