import math
def pizza(halkaisija, hinta):
    pintaAla = math.pi * (halkaisija/2)**2
    return hinta / pintaAla


pizza1_halkaisija = int(input("Anna ensimmäisen pizzan halkaisija: "))
pizza1_hinta = int(input("Anna ensimmäisen pizzan hinta: "))
pizza1 = pizza(pizza1_halkaisija, pizza1_hinta)

pizza2_halkaisija = int(input("Anna toisen pizzan halkaisija: "))
pizza2_hinta = int(input("Anna toisen pizzan hinta: "))
pizza2 = pizza(pizza2_halkaisija, pizza2_hinta)


if pizza1 < pizza2:
    print("Ensimmäisellä pizzalla on alhaisempi yksikköhinta. " + str(pizza1))
elif pizza1 > pizza2:
    print("Toisella pizzalla on alhaisempi yksikköhinta. " + str(pizza2))