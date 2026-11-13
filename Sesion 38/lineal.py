def mayor(lista):
    m = lista[0]
    for x in lista:        # recorre los n elementos una vez
        if x > m:
            m = x
    return m