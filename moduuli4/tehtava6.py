import random

N = int(input("Anna arvottavien pisteiden määrä: "))
#Ympyröiden sisäl olevat pisteet
n = 0

for i in range(N):
    x = random.random()
    y = random.random()
    if x*x + y*y <= 1:
        n += 1

print(f"Piin likiarvo on {4 *n/N}")
