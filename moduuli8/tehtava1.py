import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )
def haeLentokentatMaasta(icao):
   # sql = f"SELECT name FROM airport WHERE iso_country = '{maa}';"
    sql = "SELECT name From airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchall()
    return tulos

syote = input("Kerro ICAO koodi: ").upper()
kentat = haeLentokentatMaasta(syote)

for rivi in kentat:
    print(rivi['name'])