luku = int(input("Anna kokonaisluku: "))

alkuluku = True

if(luku <= 1):
    print("syötä toinen luku: ")

for i in range(2, luku):
    if (luku % i == 0):
        alkuluku = False
        break;

if alkuluku == True:
    print(f"{luku} on alkuluku")
else:
    print(f"{luku} ei ole alkuluku")