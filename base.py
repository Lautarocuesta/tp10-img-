import numpy as np
from PIL import Image
import time
import matplotlib.pyplot as plt

def busqueda_en_imagen(imagen, tono):
    posiciones = {}
    for y in range(imagen.shape[0]):
        for x in range(imagen.shape[1]):
            if imagen[y, x] == tono:
                posiciones[(x, y)] = tono
    return posiciones

def cargar_imagen(path):
    imagen = Image.open(path).convert('L')
    return np.array(imagen)

path = 'mmom.png'  # Ruta de tu imagen
imagen = cargar_imagen(path)
tono = 128
resultados = busqueda_en_imagen(imagen, tono)
print(resultados)

def medir_tiempo_ejecucion(imagen, tono):
    inicio = time.time()
    _ = busqueda_en_imagen(imagen, tono)
    fin = time.time()
    return fin - inicio

tiempo = medir_tiempo_ejecucion(imagen, tono)
print(f"Tiempo de ejecución: {tiempo} segundos")


def graficar_resultados(tamanos, tiempos):
    plt.plot(tamanos, tiempos, marker='o')
    plt.xlabel('Tamaño de la imagen (n x n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución de la búsqueda en imágenes')
    plt.show()

# Ejemplo con diferentes tamaños de imágenes generadas aleatoriamente
tamanos = [100, 500, 1000]
imagenes = [np.random.randint(0, 256, size=(t, t)) for t in tamanos]
tiempos = [medir_tiempo_ejecucion(imagen, tono) for imagen in imagenes]

graficar_resultados(tamanos, tiempos)

def mostrar_puntos_en_imagen(imagen, posiciones):
    plt.imshow(imagen, cmap='gray')
    y, x = zip(*posiciones.keys())
    plt.scatter(x, y, color='red', s=1)
    plt.title('Puntos encontrados')
    plt.show()

# Mostrar puntos encontrados en la imagen cargada
mostrar_puntos_en_imagen(imagen, resultados)
