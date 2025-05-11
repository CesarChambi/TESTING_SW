from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# Ir a la página de Amazon
driver.get("https://www.amazon.com")
sleep(30)

# IMPORTANTE - LEER
# Le ponemos 30 segundos porque te pedira que ingreses caracteres cuando ingrese la pagina, 
# esto se esta haciendo manual "Type the characters you see in this image"

# Buscar cartucheras 
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("cartucheras")
search_box.submit()
sleep(7)

# Hacer clic para agregar un producto al carrito
elemento = driver.find_element(By.XPATH, '//*[@id="a-autoid-5-announce"]')
elemento.click()
sleep(7)

# Cerrar el navegador
driver.quit()