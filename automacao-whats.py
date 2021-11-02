from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

contatos = pd.read_csv(r"D:\Usuários\Junta Militar\Downloads\arquivo.csv")
print(contatos)

for i in range(5):
    numero = contatos.loc[i, "Phone"]
    print(numero)
    navegador.get(f"https://api.whatsapp.com/send?phone={numero}&text=mensagem aqui")
    time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="action-button"]').click()
    time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(5)

