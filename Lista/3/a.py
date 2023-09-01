import numpy as np

# Definimos una lista
mi_lista = np.array([2, 4, 5, 7, 5, 9])

# Buscamos el elemento 5 en la lista
elemento = 5
indices = np.where(mi_lista == elemento)  # Esto devuelve un arreglo de índices donde se encuentra el elemento

# Obtenemos la primera posición (basada en 0) donde se encuentra el elemento
primera_posicion = indices[0][0]  # Accedemos al primer elemento del arreglo de índices

# Ajustamos la posición a una numeración basada en 1
posicion_en_lista = primera_posicion + 1

# Imprimimos la posición
print(f"El elemento {elemento} se encuentra en la posición {posicion_en_lista} de la lista.")