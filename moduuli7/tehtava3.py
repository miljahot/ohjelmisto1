lentoasemat = {"EFHK": "Helsinki-Vantaan lentoasema"}

syote = None
while syote != "lopeta":
    print("Kirjoita 'uusi' jos haluat syöttää uuden lentoaseman,\n'haku' jos haluat hakea jo syötetyn lentoaseman tiedot,\n'lopeta' jos haluat lopettaa?")
    syote = input()
    if syote == "uusi":
        ICAO_koodi = str(input("Anna ICAO-koodi: "))
        lentoasema = str(input("Anna lentoaseman nimi: "))
        lentoasemat[ICAO_koodi.upper()] = lentoasema
    elif syote == "haku":
        haku = str(input("Anna haettava ICAO-koodi:")).upper()
        if haku in lentoasemat:
            print(lentoasemat[haku])



