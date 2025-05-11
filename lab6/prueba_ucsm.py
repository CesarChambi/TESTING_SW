from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

#Ir a la pagina de la https://ucsm.edu.pe
driver.get("https://ucsm.edu.pe")
sleep(2)

#aceptar cookies
 #Localizar y hacer clic en el botón "Acepto"
accept_button = driver.find_element(By.ID, "euCookieAcceptWP")
accept_button.click()
sleep(2)

#en admision - convenio cooperacion interinstucional
#hacer click en "ver mas"
driver.find_element(By.XPATH, '//*[@id="Content"]/div/main/div/section[1]/div/div/div/section[2]/div/div/div/div[2]/div/div/div/div[1]/div/section/div/div/div/section[2]/div/div/div/div[2]/div/h2/a').click()
sleep(6)

