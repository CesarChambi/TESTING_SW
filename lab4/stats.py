# Actividad 3:
# Logra una cobertura de código por instrucciones completa, vale decir que todas las líneas
# del siguiente código se ejecuten, agregando los casos de prueba necesarios y llamando a la
# función stats().

def stats(lst):
    min_val = None
    max_val = None
    freq = {}

    for i in lst:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    lst_sorted = sorted(lst)
    if len(lst_sorted) % 2 == 0:
        middle = len(lst_sorted) // 2
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        median = lst_sorted[len(lst_sorted) // 2]

    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    return {
        "min": min_val,
        "max": max_val,
        "median": median,
        "mode": sorted(mode)
    }

# Ejercicio 4:
# Agrega un error manualmente al código anterior tal que tus casos de test anteriores no lo
# detecten. Luego agrega un caso de test más que si que lo detecte.
def stats2(lst):
    min_val = None
    max_val = None
    freq = {}

    for i in lst:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    lst_sorted = sorted(lst)
    if len(lst_sorted) % 2 == 0:
        middle = len(lst_sorted) // 2
        median = (lst_sorted[middle] + lst_sorted[middle + 1]) / 2  # error se cambio [middle - 1] a [middle + 1]
    else:
        median = lst_sorted[len(lst_sorted) // 2]

    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    return {
        "min": min_val,
        "max": max_val,
        "median": median,
        "mode": sorted(mode)
    }
