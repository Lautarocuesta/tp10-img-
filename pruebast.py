def medir_tiempo_ejecucion(imagen, tono):
    inicio = time.time()
    _ = busqueda_en_imagen(imagen, tono)
    fin = time.time()
    return fin - inicio

# Probar con una imagen cargada
tiempo = medir_tiempo_ejecucion(imagen, tono)
print(f"Tiempo de ejecución: {tiempo} segundos")