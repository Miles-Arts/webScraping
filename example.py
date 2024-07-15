import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = ''
path_driver = os.chdir('C:\Users\gratn\Documents\chromedriver')
driver = webdriver.Chrome(executable_path = 'webdriver')
time.sleep(10)

print("Hola")
