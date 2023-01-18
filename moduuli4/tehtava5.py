
TUNNUS = "python"
SALASANA = "rules"
i = 0
while i <= 4:
    ktunnus = input("Anna käyttäjätunnus: ")
    ksalasana = input("Anna salasana: ")

    if ktunnus == TUNNUS and ksalasana == SALASANA:
        print("Tervetuloa")
        break

    else:
        print("Pääsy evätty")
        i+=1
