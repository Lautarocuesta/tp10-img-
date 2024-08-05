def busqueda_en_imagen(imagen, tono):
    posiciones = {}
    for y in range(imagen.shape[0]):
        for x in range(imagen.shape[1]):
            if imagen[y, x] == tono:
                posiciones[(x, y)] = tono
    return posiciones