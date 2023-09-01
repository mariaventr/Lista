import numpy as np

class Lista:
    __lista= None
    def __init__(self):
        self.__lista = np.array([])

    def Insertar(self, X, p):
        if p >= 0 and p <= len(self.__lista):
            self.__lista= np.insert(self.__lista, p, X)
        else:
            print("Posición fuera de rango.")

    def Suprimir(self, p):
        if p >= 0 and p < len(self.__lista):
            self.__lista=np.delete(self.__lista, p)
        else:
            print("Posición fuera de rango.")

    def Recuperar(self, p):
        if p >= 0 and p < len(self.__lista):
            return self.__lista[p]
        else:
            print("Posición fuera de rango.")
            return None

    def Buscar(self, X):
        i=0
        while i < len(self.__lista):
            if self.__lista[i]==X:
                return i
            i+=1
        else:
            return -1

    def Primer_elemento(self):
        if len(self.__lista) > 0:
            return self.__lista[0]
        else:
            print("La lista está vacía.")
            return None

    def Ultimo_elemento(self):
        if len(self.__lista) > 0:
            return self.__lista[-1]
        else:
            print("La lista está vacía.")
            return None

    def Siguiente(self, p):
        if p >= 0 and p < len(self.__lista) - 1:
            return p + 1
        else:
            print("Posición fuera de rango para la posicion Siguiente.")
            return None

    def Anterior(self, p):
        if p > 0 and p < len(self.__lista):
            return p - 1
        else:
            print("Posición fuera de rango para la posicion Anterior.")
            return None

    def Recorrer(self):
        for elemento in self.__lista:
            print(elemento)


mi_lista = Lista()

mi_lista.Insertar(10, 0)
mi_lista.Insertar(20, 1)
mi_lista.Insertar(30, 2)


print("Elementos de la lista:")
mi_lista.Recorrer()


mi_lista.Suprimir(1)
print("Elementos de la lista después de suprimir:")
mi_lista.Recorrer()


elemento = mi_lista.Recuperar(1)
print(f"Elemento en la posición 1: {elemento}")


posicion = mi_lista.Buscar(10)
if posicion != -1:
    print(f"El elemento 10 se encuentra en la posición {posicion}")
else:
    print("El elemento 10 no se encuentra en la lista")


primer_elemento = mi_lista.Primer_elemento()
ultimo_elemento = mi_lista.Ultimo_elemento()
print(f"Primer elemento: {primer_elemento}, Último elemento: {ultimo_elemento}")


posicion = 0
posicion_siguiente = mi_lista.Siguiente(posicion)
posicion_anterior = mi_lista.Anterior(posicion)
print(f"Posición actual: {posicion}, Posición siguiente: {posicion_siguiente}, Posición anterior: {posicion_anterior}")



