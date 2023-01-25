import random
def noppa(tahkot):
    noppaluku = random.randint(1, tahkot)
    print(noppaluku)
    return noppaluku

syote = int(input("Anna nopan tahkojen määrä: "))
while True:
    if noppa(syote) == syote:
        break
    else:
        continue
