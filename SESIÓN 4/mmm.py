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
        middle = len(lst_sorted) / 2
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        middle = len(lst_sorted) / 2  
        median = lst_sorted[int(middle)]

    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i

    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    print("list = " + str(lst))
    print("min = " + str(min_val))
    print("max = " + str(max_val))
    print("median = " + str(median))
    print("mode(s) = " + str(mode))

def test():
    # Prueba con lista impar
    print("Prueba 1: Lista impar")
    stats([1, 2, 3, 4, 5])  # Mínimo, máximo, mediana (impar), una moda

    # Prueba con lista par
    print("\nPrueba 2: Lista par")
    stats([1, 2, 2, 3, 3, 4])  # Mínimo, máximo, mediana (par), dos modas

    # Prueba con todos los elementos iguales
    print("\nPrueba 3: Todos iguales")
    stats([7, 7, 7, 7])  # Mínimo, máximo, mediana, una moda (todos iguales)

    # Prueba con lista de un solo número
    print("\nPrueba 4: Lista con un solo número")
    stats([42])  # Mínimo, máximo, mediana (solo un elemento), una moda

    # Caso para verificar la mediana en una lista par
    print("\nPrueba 5: Lista par con mediana correcta")
    stats([1, 2, 3, 4, 5, 6])  # Lista par, la mediana debe ser 3.5

    # Caso para verificar la mediana en una lista con un número impar de elementos
    print("\nPrueba 6: Lista con mediana en número impar")
    stats([10, 20, 30, 40, 50])  # La mediana debe ser 30

    # Caso con lista con elementos negativos
    print("\nPrueba 7: Lista con elementos negativos")
    stats([-10, -5, 0, 5, 10])  # La mediana debe ser 0

    # Caso con lista con números flotantes
    print("\nPrueba 8: Lista con números flotantes")
    stats([1.5, 2.5, 3.5, 4.5, 5.5])  # La mediana debe ser 3.5

test()