LITRA = 3.785
def bensiini(gallons):
    gallonaLitroina = gallons * LITRA
    print(gallonaLitroina)
    return gallonaLitroina

syote = int(input("Anna ensimmäinen gallonamäärä: "))
bensiini(syote)
while True:
    syote = int(input("Anna seuraava gallonamäärä: "))
    if syote < 0:
        break
    else:
        bensiini(syote)
