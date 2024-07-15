from bs4 import BeautifulSoup
import requests
import time

#print("Entra...")

URL = 'https://scrapepark.org//courses/spanish/'

print("Analizando...")
time.sleep(0.5)

obtener_datos = requests.get(URL)
html_obtenido = obtener_datos.text #Atributo text

soup = BeautifulSoup(html_obtenido, 'html.parser') #
#print(type(soup))

primer_h2 = soup.find('h2')
print(primer_h2)
print(primer_h2.text)

h2_todos = soup.find_all('h2')
print(h2_todos)

h2_uno_solo = soup.find_all('h2', limit=1)
print(h2_uno_solo)













print("Terminado...")







