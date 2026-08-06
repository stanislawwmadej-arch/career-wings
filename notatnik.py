## nie wiem o co chodzi z json wiec robie bez
notatki = []
while True:
    print("MÓJ NOTATNIK")
    print("1. Wyświetl notatki")
    print("2. Dodaj notatkę")
    print("3. Usuń notatkę")
    print("4. Wyjdź")
    wybór = input("Wybierz co chcesz zrobić: ")
    if wybór == "1":
        if len(notatki) == 0:
            print("Nie masz jeszcze żadnych notatek.")
        else:
            print("Twoje notatki:")
            nr = 1
            for notatka in notatki:
                print(f"{nr}. {notatka}")
                nr += 1
    elif wybór == "2":
        notatka = input("Wpisz treść notatki: ")
        notatki.append(notatka)
    elif wybór == "3":
        if len(notatki) == 0:
            print("Nie masz notatek do usunięcia.")
        else:
            print("Twoje notatki:")
            nr = 1
            for notatka in notatki:
                print(f"{nr}. {notatka}")
                nr += 1
            usun = int(input("Podaj numer notatki, którą chcesz usunąć: "))
            if usun < 1 or usun > len(notatki):
                print("Nie ma takiej notatki.")
            else:
                del notatki[usun - 1]
                print("Notatka została usunięta.")
    elif wybór == "4":
        print("Na razie!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")