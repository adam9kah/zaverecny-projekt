from pojistenec import Pojistenec

class System:

    def __init__(self):
        self.pojistenci = []

    def pridani_pojistence(self):
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení pojištěného: ")
        vek = input("Zadejte věk pojištěného: ")
        tel_cislo = input("Zadejte telefonní číslo pojištěného: ")
        pojistenec = Pojistenec(jmeno, prijmeni, vek, tel_cislo)
        self.pojistenci.append(pojistenec)

    def vypsani_pojistencu(self):
        for pojistenec in self.pojistenci:
            print(pojistenec)

    def pocet_pojistencu(self):
        pocet = len(self.pojistenci)
        if pocet == 1:
            print(f"V systému je zaevidován {pocet} pojištěnec:\n")
        elif pocet == 2 or pocet == 3 or pocet == 4:
            print(f"V systému jsou zaevidováni {pocet} pojištěnci:\n")
        else:
            print(f"V systému je zaevidováno {pocet} pojištěnců:\n")

    def vyhledani_pojistence(self):
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení pojištěného: ")
        hledany_pojistenec = ""
        for pojistenec in self.pojistenci:
            if pojistenec.kontrola_jmena(jmeno, prijmeni):
                hledany_pojistenec = pojistenec
        if hledany_pojistenec != "":
            print(hledany_pojistenec)
        else:
            print("Tento pojištěnec není v systému zaevidován")