import math

# Codigo sin corregir
def isPrime(number):
    if number == 2:
        return True
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):  # Error en el rango
        if (number % check) == 0:
            return False
    return True

#Implementación correcta de isPrime (codigo corregido)
def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):  # +1 para incluir el limite
        if number % i == 0:
            return False
    return True
