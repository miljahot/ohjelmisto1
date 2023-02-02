import mysql.connector
from geopy.distance import great_circle

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

def vertaa(eka):
    sql = "SELECT latitude_deg, longitude_deg FROM airport where ident ='" + eka + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0 :
        for rivi in tulos:
            lentokentta1 = rivi[0], rivi [1]
    return lentokentta1

syote = None
while syote != "":
    syote = str(input("Anna ensimmäinen ICAO-koodi: "))
    lentokentta1 = vertaa(syote)
    toinenSyote = str(input("Anna toinen ICAO-koodi: "))
    lentokentta2 = vertaa(toinenSyote)
    print(f"Välimatka lentokentillä on: {great_circle(lentokentta1, lentokentta2).km}km")