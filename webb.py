import requests 
from bs4 import BeautifulSoup

url = 'https://listado.mercadolibre.com.co/tenis'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    productos = soup.find_all('div', class_='ui-search-item__group ui-search-item__group--title')

    for producto in productos:
         titulo = producto.find('h2', class_='ui-search-item__title')
         if titulo:
           print(titulo.text.strip())
          
    for producto in productos:
        marca = producto.find('span', class_='ui-search-item__brand-discoverability ui-search-item__group__element')
        if marca:
            print(marca.text.strip())          

    # print(len(productos))
    print("Obtuvimos la pagina")
else:
    print("Error al cargar la web, código:", response.status_code)




