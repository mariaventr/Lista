import numpy as np

class ListaSecuencial:
    __lista=None
    def __init__(self):
        self.__lista = np.array([])

    def vacia(self):
        return len(self.__lista) == 0

    def crear(self):
        self.__lista = np.array([])

    def insertar(self, elemento, posicion):
        if posicion <= 0:
            posicion = 1
        elif posicion > len(self.__lista) + 1:
            posicion = len(self.__lista) + 1
        self.__lista = np.insert(self.__lista, posicion - 1, elemento)

    def suprimir(self, posicion):
        resultado = None
        if 1 <= posicion <= len(self.__lista):
            resultado = self.__lista[posicion - 1]
            self.__lista = np.delete(self.__lista, posicion - 1)
        return resultado

    def recuperar(self, posicion):
        resultado = None
        if 1 <= posicion <= len(self.__lista):
            resultado = self.__lista[posicion - 1]
        return resultado

    def buscar(self, elemento):
        resultado = None
        if elemento in self.__lista:
            resultado = np.where(self.__lista == elemento)[0][0] + 1
        return resultado

    def primer_elemento(self):
        resultado = None
        if len(self.__lista) > 0:
            resultado = self.__lista[0]
        return resultado

    def ultimo_elemento(self):
        resultado = None
        if len(self.__lista) > 0:
            resultado = self.__lista[-1]
        return resultado

    def siguiente_posicion(self, posicion):
        resultado = None
        if 1 <= posicion < len(self.__lista):
            resultado = posicion + 1
        return resultado

    def anterior_posicion(self, posicion):
        resultado = None
        if 2 <= posicion <= len(self.__lista):
            resultado = posicion - 1
        return resultado

    def recorrer(self):
        return self.__lista.tolist()

mi_lista = ListaSecuencial()

mi_lista.insertar(10, 0)
mi_lista.insertar(20, 1)
mi_lista.insertar(30, 2)

print("Lista actual:", mi_lista.recorrer())

print("Recuperar elemento en posición 2:", mi_lista.recuperar(2))
print("Buscar elemento '20':", mi_lista.buscar(20))

mi_lista.suprimir(2)
print("Lista actual después de suprimir elemento en posición 2:", mi_lista.recorrer())


