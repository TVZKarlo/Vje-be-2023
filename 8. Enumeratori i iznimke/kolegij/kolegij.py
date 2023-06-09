class Kolegij:
    def __init__(self, ime, ECTS):
        self.__ime = ime
        self.__ECTS = ECTS

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def ECTS(self):
        return self.__ECTS

    @ECTS.setter
    def ECTS(self, ECTS):
        self.__ECTS = ECTS

    def ispis(self):
        print(f"\tKolegij {self.ime} nosi {self.ECTS} ECTS bodova")