def mostrar_parejas(lista):
    for a in lista:          # n vueltas
        for b in lista:      # n vueltas por cada vuelta externa
            print(a, b)      # se ejecuta n × n = n² veces