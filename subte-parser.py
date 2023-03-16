from bs4 import BeautifulSoup
import requests

url = "https://buenosaires.gob.ar/subte"
response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

divs = soup.find_all(id="LineaB")

estados = soup.find_all("div", class_="linea-info")

for est in estados:
    print("ESTADO:")
    print(est.contents)