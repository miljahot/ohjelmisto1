import random
x = random.randint(1, 10)

while True:
    syote = int((input("Anna luku: ")))
    if syote > x:
        print("Liian suuri arvaus")
    elif syote < x:
        print("Liian pieni arvaus")
    elif syote == x:
        print("Oikein")
        break
