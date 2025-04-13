from stats import stats, stats2

# Actividad 3: Pruebas para stats
def test_impar_sin_repetidos():
    result = stats([1, 2, 3])
    assert result == {"min": 1, "max": 3, "median": 2, "mode": [1, 2, 3]}
    result = stats([4, 2, 1, 3])
    assert result == {"min": 1, "max": 4, "median": 2.5, "mode": [1, 2, 3, 4]}

def test_moda_unica():
    result = stats([1, 2, 2, 3, 3, 3])
    assert result == {"min": 1, "max": 3, "median": 2.5, "mode": [3]}

def test_todos_iguales():
    result = stats([5, 5, 5, 5])
    assert result == {"min": 5, "max": 5, "median": 5.0, "mode": [5]}

def test_modas_empatadas():
    result = stats([1, 2, 2, 3, 3])
    assert result == {"min": 1, "max": 3, "median": 2, "mode": [2, 3]}

# Actividad 4: Pruebas para stats2
def test_impar_sin_repetidos_stats2():
    result = stats2([1, 2, 3])
    assert result == {"min": 1, "max": 3, "median": 2, "mode": [1, 2, 3]}
    result = stats2([4, 2, 1, 3])
    assert result == {"min": 1, "max": 4, "median": 2.5, "mode": [1, 2, 3, 4]}

def test_moda_unica_stats2():
    result = stats2([1, 2, 2, 3, 3, 3])
    assert result == {"min": 1, "max": 3, "median": 2.5, "mode": [3]}

def test_todos_iguales_stats2():
    result = stats2([5, 5, 5, 5])
    assert result == {"min": 5, "max": 5, "median": 5.0, "mode": [5]}

def test_modas_empatadas_stats2():
    result = stats2([1, 2, 2, 3, 3])
    assert result == {"min": 1, "max": 3, "median": 2, "mode": [2, 3]}

def test_mediana_par_incorrecta_stats2():
    # Lista par ordenada: [1, 2, 3, 4] → Mediana correcta es (2 + 3)/2 = 2.5
    result = stats2([4, 2, 1, 3])
    assert result["median"] == 2.5  # Este test detectará el error en median si el índice está mal

