SUKUPUOLI = input("Anna biologinen sukupuolesi: ")
HEMOGLOBIINI = float(input("Anna hemoglobiini arvosi (g/l): "))

nainen_alin = 117
nainen_ylin = 175
miehen_alin = 134
miehen_ylin = 195

if SUKUPUOLI == "nainen":
    if HEMOGLOBIINI >= nainen_ylin:
        print("Hemoglobiiniarvo on korkea.")
    elif HEMOGLOBIINI <= nainen_alin:
        print("Hemoglobiiniarvo on alhainen")
    else:
        print("Hemoglobiiniarvo on normaali.")

if SUKUPUOLI == "mies":
    if HEMOGLOBIINI >= miehen_ylin:
        print("Hemoglobiiniarvo on korkea.")
    elif HEMOGLOBIINI <= miehen_alin:
        print("Hemoglobiiniarvo on alhainen")
    else:
        print("Hemoglobiiniarvo on normaali.")