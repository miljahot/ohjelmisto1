import random
def noppa():
    noppaluku = random.randint(1, 6)
    print(noppaluku)
    return noppaluku

while True:
    if noppa() == 6:
        break
    else:
        continue
