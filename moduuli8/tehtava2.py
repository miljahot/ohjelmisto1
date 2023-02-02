import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

def haeLentokentatMaasta(maa):
    sql = "SELECT type, COUNT(type) FROM airport WHERE iso_country = %s GROUP BY type"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (maa,))
    tulos = kursori.fetchall()
    return tulos

syote = input("Kerro maakoodi: ").upper()
kentat = haeLentokentatMaasta(syote)

for rivi in kentat:
    print(rivi)