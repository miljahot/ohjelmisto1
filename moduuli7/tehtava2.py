syote = None
nimet = set()
syote = input("Anna nimi: ")
while syote != "":
    if syote in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(syote)

    syote = input("Anna nimi: ")

for nimi in nimet:
    print(nimi)
    