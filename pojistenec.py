class Pojistenec:

    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):
        return f"Jmeno: {self.jmeno}\nPříjmení: {self.prijmeni}\nVěk: {self.vek}\nTelefonní číslo: {self.tel_cislo}\n"

    def kontrola_jmena(self, jmeno, prijmeni):
        if jmeno == self.jmeno and prijmeni == self.prijmeni:
            return True
        return False