# Actividad 5:
from add8 import add8

def test():
    # Caso 1: Todos ceros
    assert add8(0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0) == (False,)*8 + (False,)

    # Caso 2: Alternando bits sin carry
    add8(1,0,1,0,1,0,1,0, 0,1,0,1,0,1,0,1, 0)

    # Caso 3: Alternando bits con carry inicial
    add8(1,0,1,0,1,0,1,0, 0,1,0,1,0,1,0,1, 1)

    # Caso 4: Todos unos, sin carry
    add8(1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, 0)

    # Caso 5: Uno o dos bits distintos para ramas extra
    add8(1,0,0,0,0,0,0,0, 1,1,0,0,0,0,0,0, 0)

