from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

myUrl = 'https://es.wikipedia.org/wiki/Masters_de_Madrid'

# Conectarse al servidor y obtener la pagina
uClient = urlopen(myUrl)
pagina_html = uClient.read()
uClient.close()

#html parsing
pagina_soup = BeautifulSoup(pagina_html, "html.parser")

#Datos
tabla = pagina_soup.findAll("table")
tabla_body = tabla[3].find('tbody')

data = []
rows = tabla_body.find_all('tr')
rows = rows[17:(len(rows) - 1)]

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Para quitar los espacios

with open("rolandGarros.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for row in data:
        wr.writerow(row)

#exec(open("script.py").read())

