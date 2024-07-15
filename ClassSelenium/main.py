from files_otros.store_selernium import Store_Selenium

with Store_Selenium() as bot:
    bot.get_url()
    bot.rellenar_form()

print("Hola")    