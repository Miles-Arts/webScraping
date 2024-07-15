from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
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

for seccion in h2_todos:
    print(seccion.text)

for seccion in h2_todos:
    print(seccion.get_text(strip = True))



#print(seccion.find_all(class_ = "heading-container heading-center"))

# divs = soup.find_all(class_ = 'heading-container heading-center')
# for div in divs:
#     print(div)
#     print(" ")

divs = soup.find_all('div', class_ = 'heading-container heading-center')
for div in divs:
    print(div)
    print(" ")


src_todos = soup.find_all(src = True)
for elemento in src_todos:
    if elemento['src'].endswith(".jpg"):
        print(elemento)

#print(src_todos.get_text(strip = True))        


url_imagenes = []

for i, imagen in enumerate(src_todos):

    if imagen['src'].endswith('png'):
        
        print(imagen['src'])
        r = requests.get(f'https://scrapepark.org//courses/spanish/{imagen['src']}')

        with open(f'imagen_{i}.png', 'wb') as f:
            f.write(r.content)












print("Terminado...")







