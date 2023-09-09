class Komponenta:

    def __init__(self, kategorija, PN, cijena):
        self.__kategorija = kategorija
        self.__PN = PN
        self.__cijena = cijena

    @property
    def kategorija(self):
        return self.__kategorija

    @kategorija.setter
    def ime(self, kategorija):
        self.__kategorija = kategorija

    @property
    def PN(self):
        return self.__PN

    @PN.setter
    def PN(self, PN):
        self.__PN = PN

    @property
    def cijena(self):
        return self.__cijena

    @cijena.setter
    def cijena(self, cijena):
        self.__cijena = cijena


    def ispis(self):
      print("Informacije o elektroničkoj komponenti: ")
      print(f'\tKategorija: {self.__kategorija}')
      print(f'\tPart number: {self.__PN}')
      print(f'\tCijena: {self.__cijena}')

