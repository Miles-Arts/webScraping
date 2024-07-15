# import requests 
# from bs4 import BeautifulSoup

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Edge()

url = 'https://www.google.com'

# response = requests.get(url)

driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

productos = soup.find_all('div', class_='container-item ad-pb1 thumbail ad-une')

for producto in productos:
    marca = producto.find('span', class_='title')
    if marca:
        print(marca.text.strip())    

    print(len(productos))

    print("Obtuvimos la pagina")
else:
    print("Error al cargar la web")

