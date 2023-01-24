import random

noppa_maara = int(input("Anna arpakuutioiden lukumäärä: "))

n = 0
for i in range(noppa_maara):
    n = n + random.randint(1, 6)

print(n)