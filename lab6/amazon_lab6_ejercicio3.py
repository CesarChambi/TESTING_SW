from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Variables que usaremos en todas las pruebas
mi_producto = "cartucheras"
driver = webdriver.Chrome()

# prueba 1: Busqueda normal
driver.get("https://www.amazon.com")
sleep(30)

# IMPORTANTE - LEER
# Le ponemos 30 segundos porque te pedira que ingreses caracteres cuando ingrese la pagina, 
# esto se esta haciendo manual "Type the characters you see in this image"

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(mi_producto)
search_box.submit()
sleep(5)

# prueba 2: usaremos la misma variable para la segunda busqueda
driver.get("https://www.amazon.com")
sleep(2)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(mi_producto + " escolares")  # reutilizamos la variable
search_box.submit()
sleep(5)

# prueba 3: Agregar al carrito
driver.find_element(By.XPATH, '//*[@id="a-autoid-5-announce"]').click()
sleep(3)

print(f"Todas las pruebas usaron: {mi_producto}")
driver.quit()