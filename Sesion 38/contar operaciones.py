def sumar_lista(numeros):
    total = 0                 # 1 operación
    for x in numeros:         # se repite n veces
        total = total + x     # 1 operación por vuelta → n operaciones
    return total              # 1 operación

# Total aproximado: n + 2 operaciones