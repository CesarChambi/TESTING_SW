from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://youtube.com')

cuadro_busqueda = driver.find_element(By.NAME, 'search_query')

cuadro_busqueda.send_keys(':V')

cuadro_busqueda.click()

sleep(5)

#Ir a la pagina de la https://ucsm.edu.pe
#aceptar cookies
#en admision - convenio cooperacion interinstucional
#hacer click en "ver mas"
#corroborar que la informacion de modal 