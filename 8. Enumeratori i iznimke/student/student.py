from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, ime, prezime, ispit):
        self.ime = ime
        self.prezime = prezime
        self.ispit = ispit

    @abstractmethod
    def ispis(self):
        pass