class Projekt:

    def __init__(self, datum, opis, trošak):
        self.__datum = datum
        self.__opis = opis
        self.__trošak = trošak


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
    def trošak(self):
        return self.__trošak

    @trošak.setter
    def trošak(self, trošak):
        self.__trošak = trošak


    def ispis(self):
        print("Informacije o projektu: ")
        print(f'\tDatum: {self.__datum}')
        print(f'\tOpis: {self.__opis}')
        print(f'\tTrošak: {self.__trošak}')
