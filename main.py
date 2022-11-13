from system import System

system = System()
print("---Evidence pojištěnců---\n")
pokracovat = True
while pokracovat:
    volba = input("Co si přejete provést?\n1 - Přidat nového pojištěnce\n2 - Vypsat všechny pojištěnce\n3 - Vyhledat pojištěnce\n4 - Konec\n")
    if volba == "1":
        system.pridani_pojistence()
    elif volba == "2":
        system.pocet_pojistencu()
        system.vypsani_pojistencu()
    elif volba == "3":
        system.vyhledani_pojistence()
    elif volba == "4":
        pokracovat = False
    else:
        print(f"S vámi zadanou volbou {volba} nelze provést žádnou akci. Zvolte z možností 1 - 4.")