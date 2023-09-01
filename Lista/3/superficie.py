"""En el ejercicio Nº 3, se necesita procesar datos relacionados con incendios forestales, 
específicamente el nombre de la provincia y la superficie total afectada. 
Para este tipo de tarea, se recomienda la implementación de un T.A.D 
(Tipo Abstracto de Datos) lista por contenido, que permita almacenar y 
procesar estos datos de manera eficiente.

Justificación de la elección del T.A.D lista por contenido:
1. **Acceso a datos específicos:** Necesitamos acceder a elementos específicos de los datos, 
en este caso, el nombre de la provincia y la superficie total afectada. Un T.A.D lista 
por contenido permite acceder a elementos de la lista por su contenido directamente, 
lo que facilita la búsqueda y recuperación de estos datos específicos.

2. **Ordenación:** También se requiere ordenar los datos por superficie total afectada de mayor 
a menor. Un T.A.D lista por contenido se puede utilizar junto con algoritmos de ordenación para 
lograr esto de manera eficiente.

3. **Flexibilidad:** Un T.A.D lista por contenido es flexible y puede adaptarse a diferentes tipos de 
datos, lo que lo hace adecuado para trabajar con datos heterogéneos como los proporcionados en un 
conjunto de datos CSV.

En resumen, para procesar los datos del archivo CSV que contienen información sobre 
incendios forestales y obtener una lista ordenada de provincias y superficies afectadas, 
se recomienda utilizar un T.A.D lista por contenido."""


import csv
import numpy as np

class ListaSecuencialPorContenido:
    def __init__(self):
        self.lista = np.array([])

    def insertar(self, elemento):
        self.lista = np.append(self.lista, elemento)

    def suprimir(self, elemento):
        if elemento in self.lista:
            self.lista = self.lista[self.lista != elemento]

    def recuperar(self, posicion):
        if 1 <= posicion <= len(self.lista):
            return self.lista[posicion - 1]
        else:
            return None

    def buscar(self, elemento):
        if elemento in self.lista:
            return np.where(self.lista == elemento)[0][0] + 1
        else:
            return None

    def primer_elemento(self):
        if len(self.lista) > 0:
            return self.lista[0]
        else:
            return None

    def ultimo_elemento(self):
        if len(self.lista) > 0:
            return self.lista[-1]
        else:
            return None

    def siguiente_elemento(self, elemento):
        if elemento in self.lista:
            index = np.where(self.lista == elemento)[0][0]
            if index < len(self.lista) - 1:
                return self.lista[index + 1]
        return None

    def anterior_elemento(self, elemento):
        if elemento in self.lista:
            index = np.where(self.lista == elemento)[0][0]
            if index > 0:
                return self.lista[index - 1]
        return None

    def recorrer(self):
        return self.lista

    def cargar_desde_csv(self, archivo_csv):
        with open(archivo_csv, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            lista_provincias_superficie = []  # Creamos una lista temporal para almacenar los pares provincia-superficie

            for row in reader:
                nombre_provincia = row[3]
                superficie_str = row[6].replace(',', '.')

                if superficie_str:
                    superficie_afectada = float(superficie_str)
                    lista_provincias_superficie.append((nombre_provincia, superficie_afectada))

            # Una vez que hemos recopilado todos los pares, asignamos la lista a mi_lista.lista
            self.lista = lista_provincias_superficie

    def calcular_superficie_por_provincia(self):
        # Usaremos un diccionario para acumular la superficie por provincia
        superficie_por_provincia = {}
        for provincia, superficie in self.lista:
            if provincia in superficie_por_provincia:
                superficie_por_provincia[provincia] += superficie
            else:
                superficie_por_provincia[provincia] = superficie

        # Devolvemos la suma total y los nombres de las provincias con su superficie
        return superficie_por_provincia


mi_lista=ListaSecuencialPorContenido()
mi_lista.cargar_desde_csv('superficie.csv')
mi_lista.lista = sorted(mi_lista.lista, key=lambda x: x[1], reverse=True)

print("ITEM C")
for provincia, superficie in mi_lista.lista:
    print(f"Provincia: {provincia}, Superficie Afectada: {superficie} ha")


print("ITEM B")
superficie_por_provincia = mi_lista.calcular_superficie_por_provincia()
total_superficie = sum(superficie_por_provincia.values())
print(f"Superficie total afectada: {total_superficie} ha")
for provincia, superficie in superficie_por_provincia.items():
    print(f"Provincia: {provincia}, Superficie Afectada: {superficie} ha")


