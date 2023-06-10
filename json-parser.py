import json, requests, sqlite3
from datetime import datetime, timezone, timedelta

# Crear una timezone GMT-3 y obtener el now para GMT-3.
gmt_minus_3 = timezone(timedelta(hours=-3))
date = datetime.now(tz=gmt_minus_3)
print("--------------------------------------------\n" + "Parsing at " + str(date))
url = "http://buenosaires.gob.ar/subtes"

r = requests.get(url)

estados = r.json()['subtes']

for linea in estados:
    if(linea['estado'][0] != '\n\t\t'):
        print(linea['nombre'] + ": " + linea['estado'][0])
        
        #Creacion de DB y creacion del cursor.
        con = sqlite3.connect("/Users/bruno/Documents/subte-parser/transporte.db")
        cur = con.cursor()

        query = "INSERT INTO subte (timestamp, linea, estado, frecuencia) VALUES (?, ?, ?, ?)"
        values = (date, linea['nombre'], linea['estado'][0],linea['frecuencia'])
        cur.execute(query, values)

        con.commit()
        con.close()

