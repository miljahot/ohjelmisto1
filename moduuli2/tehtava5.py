LUOTI_KERROIN = 13.3
NAULA_KERROIN = 32 * LUOTI_KERROIN
LEIVISKÄ_KERROIN = 20 * NAULA_KERROIN

leiviskatGrammoina = float(input("Anna leiviskät: \n")) * LEIVISKÄ_KERROIN
naulatGrammoina = float(input("Anna naulat: \n")) * NAULA_KERROIN
luoditGrammoina = float(input("Anna luodit: \n")) * LUOTI_KERROIN

grammatYhteensä = leiviskatGrammoina + naulatGrammoina + luoditGrammoina
kilogrammat = grammatYhteensä / 1000
grammat = grammatYhteensä % 1000

print("Massa nykymittojen mukaan: ")
print(f"{int(kilogrammat)} kilogrammaa ja  {grammat: .2f}  grammaa.")









