import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'http://demo-store.seleniumacademy.com/'


class Store_Selenium(webdriver.Chrome):
    def __init__(self, self_path = 'C:/Users/gratn/Documents/chromedriver/webdriver', teardown = False):
        self.driver_path = self_path
        self.teardown = teardown

        super(Store_Selenium, self).__init__()
        self.maximize_window()

    # def __exit__(self, exc_type: Type[BaseException] | None, exc: BaseException | None, TracebackType | None): 
    #     return super().__exit__(exc_type, exc, traceback)   
    def __exit__(self, exce_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    #Métodos    Escribir    

    def get_url(self):
        self.get(URL)

    def rellenar_form(self):

        cuenta = self.find_element(By.XPATH, '//span[contains(text(), "Account")]' )
        cuenta.click()

        register = self.find_element(By.XPATH, '//li/a[@title = "Register"]' )
        register.click()

        #Rellenar formulario
        #name
        first_name = self.find_element(By.XPATH, '//input[@id = "firstname"]')
        first_name.send_keys('Juanita')

        #middlename
        middle_name = self.find_element(By.XPATH, '//input[@id = "middlename"]')
        middle_name.send_keys('Celeste')

        #Last Name
        last_name = self.find_element(By.XPATH, '//input[@id = "lastname"]')
        last_name.send_keys('Italia')

        #email 
        email = self.find_element(By.XPATH, '//input[@id = "email_address"]')
        email.send_keys('informacion@backmaria.com')

        #Password
        password = self.find_element(By.XPATH, '//input[@id = "password"]')
        password.send_keys('abc1234')

        #Password Confirmation
        password = self.find_element(By.XPATH, '//input[@id = "confirmation"]')
        password.send_keys('abc1234')

        #subscribed
        subscribed = self.find_element(By.XPATH, '//input[@id = "is_subscribed"]')
        subscribed.click()

        #registro
        registro = self.find_element(By.XPATH, '//button[@title = "Register"]')
        registro.click()

        #print(cuenta.text)

        time.sleep(25)

        print("Terminado...")

