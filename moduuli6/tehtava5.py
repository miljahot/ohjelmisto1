def flista(kokonaisluku):
    uusilista = []
    for i in kokonaisluku:
        if i % 2 == 0:
            uusilista.append(i)
    return uusilista

lista = [3, 5, 8, 2, 7, 9]
print("Alkuperäinen lista:")
print(lista)
print("Vain parilliset luvut sisältävä lista:")
print(flista(lista))
