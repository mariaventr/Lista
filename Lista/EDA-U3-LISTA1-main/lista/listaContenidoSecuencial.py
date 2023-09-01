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

# Ejemplo de uso
mi_lista_secuencial_por_contenido = ListaSecuencialPorContenido()
mi_lista_secuencial_por_contenido.insertar(10)
mi_lista_secuencial_por_contenido.insertar(20)
mi_lista_secuencial_por_contenido.insertar(30)
print("Lista secuencial por contenido actual:", mi_lista_secuencial_por_contenido.recorrer())
mi_lista_secuencial_por_contenido.suprimir(20)
print("Despues Suprimir:", mi_lista_secuencial_por_contenido.recorrer())


