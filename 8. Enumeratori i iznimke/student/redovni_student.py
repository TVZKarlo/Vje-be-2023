from .student import Student


class RedovniStudent(Student):
    def __init__(self, ime, prezime, ispit, broj_prijava):
        super().__init__(ime, prezime, ispit)
        self.broj_prijava = broj_prijava

    def ispis(self):
        print(f"\tRedovni student {self.ime} {self.prezime} je {self.broj_prijava}. put prijavio:")
        self.ispit.ispis()