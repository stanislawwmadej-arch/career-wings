imie = input("Podaj swoje imię: ")
rok_urodzenia = int(input("Podaj swój rok urodzenia: "))

wiekE = 65
rok = 2026

wiek = rok - rok_urodzenia
emerytura = wiekE - wiek

wiadomosc = f"czesc {imie}. Obecnie masz {wiek} lat, więc do emerytury zostało Ci {emerytura} lat."
print(wiadomosc)