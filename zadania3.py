##pierwsze zad 
punkty = {
    "Mariusz":30, "Mateusz":55, "Marta":76, "Roman":30,
    "Arleta":59, "Adrian":96, "Monika":91, "Andrzej":22,
    "Krzysztof":83, "Krystyna":93, "Piotr":44, "Dawid":10, "Agnieszka":15
}
nie_zdan = []
najlepsi = []
najwięcej = 0
najlepszy = ()
for student, wynik in punkty.items():
    if wynik <= 45:
        nie_zdan.append(student)
    elif wynik >= 91:
        najlepsi.append(student)
    if wynik > najwięcej:
        najwięcej = wynik
        najlepszy = (student, wynik)

print(f"Nie zdali: {nie_zdan}")
print(f"Najlepsi okazali się: {najlepsi}") 
print(f"Najwięcej punktów zdobył: {najlepszy}")

###drugie zad 

names = [
    'Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz',
    'Edward', 'Piotr', 'Jan', 'Denis', 'Amir', 'Igor', 'Borys',
    'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel'
]
name_dict = {}
for name in names:
    v = name_dict.get(name[0], set())
    v = v | {name}
    name_dict[name[0]] = v
print(name_dict)
#to bylo ciezsze samemu nie zrobilem ale czaje ocb
####trzecie zad
num = 30
fibonacci = []

n = 1
while len(fibonacci) < num:
    if n == 1 or n == 2:
        fibonacci.append(1)
    else:
        fibonacci.append(sum(fibonacci[-2:]))
    n = n + 1

print(fibonacci)


