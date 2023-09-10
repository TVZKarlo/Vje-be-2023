class Projekt:

    def __init__(self, datum, opis, trosak):
        self.__datum = datum
        self.__opis = opis
        self.__trosak = trosak

    @property
    def datum(self):
        return self.__datum

    @datum.setter
    def datum(self, datum):
        self.__datum = datum

    @property
    def opis(self):
        return self.__opis

    @opis.setter
    def opis(self, opis):
        self.__opis = opis

    @property
    def trosak(self):
        return self.__trosak

    @trosak.setter
    def trosak(self, trosak):
        self.__trosak = trosak


    def ispis(self):
        print("Informacije o projektu: ")
        print(f'\tDatum: {self.__datum}')
        print(f'\tOpis: {self.__opis}')
        print(f'\tTrošak: {self.__trosak}')
