import random

class Gracz:
    def __init__(self):
        self.zdrowie = 50
        self.zapas = 50
        self.amulet = False
        self.miecz = False
    
        
    def zmien_zdrowie(self, wartosc):
        self.zdrowie = max(0, self.zdrowie + wartosc)
        if self.zdrowie == 0:
            print("Twoje zdrowie spadło do zera. Przegrywasz grę!")
            exit()

    def zmien_zapas(self, wartosc):
        self.zapas = max(0, self.zapas + wartosc)
        if self.zapas == 0:
            print("Brak zapasów. Z głodu nie możesz kontynuować podróży. Przegrywasz grę!")
            exit()

    def pokaz_statystyki(self):
        print(f"Zdrowie: {self.zdrowie}, Zapas: {self.zapas}, Amulet: {'Tak' if self.amulet else 'Nie'}, Skarb: {'Tak' if self.miecz else 'Nie'}\n")
        
    def zycie(self):
        print(f"Zdrowie: {self.zdrowie}")

def walka(gracz):
    print("Napotykasz wroga! Musisz walczyć!")
    przeciwnik_zdrowie = random.randint(20, 50)
    while przeciwnik_zdrowie > 0 and gracz.zdrowie > 0:
        print(f"Zdrowie przeciwnika: {przeciwnik_zdrowie}")
        gracz.zycie()
        print("Co chcesz zrobić?\n1. Atakuj\n2. Uciekaj")
        decyzja = input("Twoja odpowiedź: ").strip()
        if decyzja == "1":
            obrazenia = random.randint(10, 15)
            if gracz.miecz:
                obrazenia += 5  # Miecz dodaje 10 do obrażeń
                print("Używasz miecza i zadajesz większe obrażenia!")
            przeciwnik_zdrowie -= obrazenia
            print(f"Zadajesz przeciwnikowi {obrazenia} obrażeń.")
            if przeciwnik_zdrowie > 0:
                obrazenia_odwetu = random.randint(5, 20)
                gracz.zmien_zdrowie(-obrazenia_odwetu)
                print(f"Przeciwnik zadaje Ci {obrazenia_odwetu} obrażeń.")
        elif decyzja == "2":
            if random.choice([True, False]):
                print("Udało Ci się uciec!")
                return
            else:
                print("Nie udało Ci się uciec! Przeciwnik atakuje.")
                obrazenia_odwetu = random.randint(5, 20)
                gracz.zmien_zdrowie(-obrazenia_odwetu)
        else:
            print("Nieprawidłowy wybór. Przeciwnik Cię atakuje!")
            obrazenia_odwetu = random.randint(5, 20)
            gracz.zmien_zdrowie(-obrazenia_odwetu)

    if przeciwnik_zdrowie <= 0:
        print("Pokonałeś przeciwnika!\n")
        gracz.zmien_zapas(20)


def gra():
    gracz = Gracz()
    print("Witaj w przygodowej grze tekstowej!")
    print("Znajdujesz się na skraju tajemniczego lasu. Twoim celem jest dotarcie do zamku na wzgórzu.")
    print("Każda decyzja wpłynie na przebieg gry. Odpowiadaj 'TAK' lub 'NIE'. Powodzenia!\n")

    # Początek gry
    print("Czy chcesz wejść do lasu?")
    decyzja1 = input("Twoja odpowiedź (TAK/NIE): ").strip().upper()

    if decyzja1 == "TAK":
        print("Wchodzisz do lasu. Drzewa szumią wokół, a powietrze jest ciężkie od tajemnic. Po chwili spotykasz starca.")
        print("Starzec pyta: 'Czy możesz pomóc mi odnaleźć moją laskę?'")
        decyzja2 = input("Twoja odpowiedź (TAK/NIE): ").strip().upper()

        if decyzja2 == "TAK":
            print("Pomagasz starcowi. W nagrodę otrzymujesz magiczny amulet, który chroni Cię przed niebezpieczeństwami.")
            gracz.amulet = True
            gracz.zmien_zdrowie(10)
        else:
            print("Starzec odwraca się plecami. Straciłeś okazję na pomoc i nagrodę.")

        gracz.pokaz_statystyki()
        print("Idąc dalej, docierasz do rozwidlenia dróg. Jeden szlak prowadzi na wzgórze, drugi do ciemnej jaskini.")
        print("Czy chcesz wejść do jaskini?")
        decyzja3 = input("Twoja odpowiedź (TAK/NIE): ").strip().upper()

        if decyzja3 == "TAK":
            if gracz.amulet:
                print("Wchodzisz do jaskini i dzięki amuletowi unikasz pułapek. Znajdujesz ukryty mityczny miecz!")
                gracz.miecz = True
                gracz.zmien_zapas(30)
            else:
                print("Wchodzisz do jaskini, ale wpadasz w pułapkę i ranisz swoją nogę.")
                gracz.zmien_zdrowie(-30)
        else:
            print("Unikasz jaskini i podążasz ścieżką na wzgórze. Po drodze spotykasz grupę wędrowców, którzy oferują Ci jedzenie.")
            gracz.zmien_zapas(20)

    else:
        print("Postanawiasz ominąć las i iść wzdłuż jego granicy. Niestety, droga jest długa i pełna przeszkód.")
        gracz.zmien_zdrowie(-20)

    gracz.pokaz_statystyki()

    # Dodatkowe losowe zdarzenie
    print("\nNagle słyszysz dziwne dźwięki w oddali. Czy chcesz sprawdzić, co się dzieje?")
    decyzja4 = input("Twoja odpowiedź (TAK/NIE): ").strip().upper()
    if decyzja4 == "TAK":
        losowe_zdarzenie = random.choice([
            ("Spotykasz leśnego ducha, który udziela Ci wskazówek!", 0, 20),
            ("Wpadasz w zasadzkę i tracisz część zapasów!", -10, -20),
            ("Znajdujesz ukryte przejście, które skraca Twoją drogę do zamku!", 10, 10),
            ("Napotykasz dzikie zwierzę i musisz walczyć!", 0, 0)
        ])
        print(losowe_zdarzenie[0])
        if "walczyć" in losowe_zdarzenie[0]:
            walka(gracz)
        else:
            gracz.zmien_zdrowie(losowe_zdarzenie[1])
            gracz.zmien_zapas(losowe_zdarzenie[2])
    else:
        print("Ignorujesz dźwięki i kontynuujesz swoją podróż.")

    gracz.pokaz_statystyki()
    
    
    losowe_zdarzenie = random.choice([
        ("Na twojej drodze staje rozbujnik, musisz walczyć!", 0, 0),
        ])
    print(losowe_zdarzenie[0])
    if "walczyć" in losowe_zdarzenie[0]:
        walka(gracz)
    else:
        gracz.zmien_zdrowie(losowe_zdarzenie[1])
        gracz.zmien_zapas(losowe_zdarzenie[2])
    gracz.pokaz_statystyki()
    
    # Kolejna decyzja
    print("Po długim marszu docierasz do rzeki. Czy chcesz spróbować ją przepłynąć?")
    decyzja5 = input("Twoja odpowiedź (TAK/NIE): ").strip().upper()
    
    if decyzja5 == "TAK":
        if random.choice([True, False]):
            print("Udaje Ci się przepłynąć rzekę bez problemów. Jesteś coraz bliżej zamku!")
            gracz.zmien_zdrowie(10)
        else:
            print("Rzeka okazuje się zdradliwa i tracisz cenne zapasy.")
            gracz.zmien_zapas(-30)
    else:
        print("Decydujesz się poszukać mostu. Znajdujesz go po długich poszukiwaniach, co opóźnia Twoją podróż.")
        gracz.zmien_zapas(-10)
        
    gracz.pokaz_statystyki()

    print("W końcu docierasz do zamku, choć Twoja przygoda była pełna wyzwań. Gratulacje!")
    print("\nKoniec gry. Dziękujemy za grę!")

# Uruchomienie gry
gra()