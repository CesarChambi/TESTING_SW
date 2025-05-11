from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# Ir a Amazon
driver.get("https://www.amazon.com")
sleep(30)

# IMPORTANTE - LEER
# Le ponemos 30 segundos porque te pedira que ingreses caracteres cuando ingrese la pagina, 
# esto se esta haciendo manual "Type the characters you see in this image"

# Lista de productos para buscar
productos = ["cartucheras", "mochilas", "libretas", "lápices"]

# Busqueda de cada producto
for producto in productos:
    # Buscar el producto
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(producto)
    search_box.submit()
    sleep(7)
    
    # Solo agregar al carrito en la primera busqueda
    if producto == productos[0]:
        elemento = driver.find_element(By.XPATH, '//*[@id="a-autoid-5-announce"]')
        elemento.click()
        sleep(7)
    
    # Volver a la pagina principal para la siguiente búsqueda
    driver.get("https://www.amazon.com")
    sleep(5)

# Cerrar navegador
driver.quit()