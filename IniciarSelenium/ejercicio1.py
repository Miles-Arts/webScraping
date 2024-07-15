import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Cargando...")

url = 'http://demo-store.seleniumacademy.com/'
path_driver = os.chdir('C:/Users/gratn/Documents/chromedriver')

#Objero Driver
driver = webdriver.Chrome()


#Obtener un UEL con Driver
#driver.maximize_window()
    # Access each dimension individually
# x = driver.get_window_position().get('x')
# y = driver.get_window_position().get('y')

#     # Or store the dimensions and query them later
# position = driver.get_window_position()
# x1 = position.get('x')
# y1 = position.get('y')
  
driver.get(url)

#Obtener Texto
texto_1 = driver.find_element(By.XPATH, '//nav/ol/li/a[contains(text(),"W")]')
print(texto_1.text)

texto_2 = driver.find_elements(By.XPATH, '//nav/ol/li/a')

for i in texto_2:
    print(i.text)


cuenta = driver.find_element(By.XPATH, '//span[contains(text(), "Account")]' )
cuenta.click()

register = driver.find_element(By.XPATH, '//li/a[@title = "Register"]' )
register.click()

#Rellenar formulario
#name
first_name = driver.find_element(By.XPATH, '//input[@id = "firstname"]')
first_name.send_keys('Juanita')

#middlename
middle_name = driver.find_element(By.XPATH, '//input[@id = "middlename"]')
middle_name.send_keys('Celeste')

#Last Name
last_name = driver.find_element(By.XPATH, '//input[@id = "lastname"]')
last_name.send_keys('Italia')

#email 
email = driver.find_element(By.XPATH, '//input[@id = "email_address"]')
email.send_keys('informacion@backmaria.com')

#Password
password = driver.find_element(By.XPATH, '//input[@id = "password"]')
password.send_keys('abc1234')

#Password Confirmation
password = driver.find_element(By.XPATH, '//input[@id = "confirmation"]')
password.send_keys('abc1234')

#subscribed
subscribed = driver.find_element(By.XPATH, '//input[@id = "is_subscribed"]')
subscribed.click()

#registro
registro = driver.find_element(By.XPATH, '//button[@title = "Register"]')
registro.click()

#print(cuenta.text)

time.sleep(25)

print("Terminado...")







