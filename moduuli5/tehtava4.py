kaupunkienLista = []
n = 0
for i in range(5):
    n += 1
    syote = input(f" {n}. Anna kaupungin nimi: ")
    kaupunkienLista.append(syote)

for x in kaupunkienLista:
    print(x)
