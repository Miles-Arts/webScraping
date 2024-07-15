import selenium
import requests
from  bs4 import BeautifulSoup
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

workbook = openpyxl.Workbook()

hoja_activa = workbook.active
driver = webdriver.Chrome()


website = 'https://www.google.com'

url = requests.get(website)
time.sleep(25)


cuenta = driver.find_element(By.XPATH, '//input[@title = "checkbox"]' )
cuenta.click()
driver.get(url)

soup = BeautifulSoup(url.content, 'html.parser' )
nombre = []

elementos_a = soup.find_all('div', class_='info-container country-co')

for elemento_h2 in elementos_a:
    elemento_a = elemento_h2.find('p')
    if elemento_a:
        nombre.append(elemento_a.text.strip())

# todo_junto = [(nombre[i]) for i in range(len(nombre))]
# for producto in todo_junto:
#     print(producto)

# for i in range(len(nombre)):
#     hoja_activa.cell(row=i+1, column=1, value=nombre[i])

#     workbook.save("nombre.xlsx")

time.sleep(25)

print("Terminado...")
