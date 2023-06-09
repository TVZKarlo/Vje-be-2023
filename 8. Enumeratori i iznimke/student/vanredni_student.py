from .student import Student
from .izracun_skolarine import IzracunSkolarine


class VanredniStudent(Student, IzracunSkolarine):
    def __init__(self, ime, prezime, ispit):
        super().__init__(ime, prezime, ispit)

    def izracun_skolarine(self):
        return self.ispit.kolegij.ECTS * 50

    def ispis(self):
        print(f"\tVanredni student {self.ime} {self.prezime} je prijavio:")
        self.ispit.ispis()
        print(f"\tPotrebno je platiti {self.izracun_skolarine()} eura")