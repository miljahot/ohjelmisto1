luku_lista = []

while True:
    luku = input("Anna luku: ")
    if luku != "":
        luku_lista.append(int(luku))
    else:
        print(f"Pienin luku: {min(luku_lista)}")
        print(f"Suurin luku: {max(luku_lista)}")
        break