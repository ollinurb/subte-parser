from bs4 import BeautifulSoup
import requests

url = "https://buenosaires.gob.ar/subte"
response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

estados = soup.find_all("div", class_="linea-info")

lineas = "ABCDEHP"
for x,est in enumerate(estados):
    print("ESTADO Linea " + lineas[x] + ":")
    print(est.contents[1].contents[0])
    print(est.contents[3].contents[0])