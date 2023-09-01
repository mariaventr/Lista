class Celda:
    def __init__(self, xitem=0, xsig=-1):
        self.__item = xitem
        self.__sig = xsig

    def poner_item(self, x):
        self.__item = x

    def obtener_item(self):
        return self.__item

    def poner_sig(self, xs):
        self.__sig = xs

    def obtener_sig(self):
        return self.__sig

class ListaEnlazadaCursor:
    def __init__(self, max_size):
        self.__espacio = [Celda() for _ in range(max_size)]
        self.__inicio = -1
        self.__cursor = -1

    def insertar(self, elemento):
        nueva_celda = self.obtener_celda_libre()
        if nueva_celda != -1:
            self.__espacio[nueva_celda].poner_item(elemento)
            if self.__cursor == -1:
                self.__inicio = nueva_celda
            else:
                self.__espacio[nueva_celda].poner_sig(self.__espacio[self.__cursor].obtener_sig())
                self.__espacio[self.__cursor].poner_sig(nueva_celda)
            self.__cursor = nueva_celda

    def suprimir(self):
        if self.__cursor != -1:
            celda_eliminada = self.__cursor
            siguiente_celda = self.__espacio[celda_eliminada].obtener_sig()
            if self.__inicio == self.__cursor:
                self.__inicio = siguiente_celda
            self.__espacio[celda_eliminada].poner_sig(-1)
            self.__cursor = siguiente_celda

    def recuperar(self):
        if self.__cursor != -1:
            return self.__espacio[self.__cursor].obtener_item()
        return None

    def buscar(self, elemento):
        cursor = self.__inicio
        posicion = 1
        while cursor != -1:
            if self.__espacio[cursor].obtener_item() == elemento:
                return posicion
            cursor = self.__espacio[cursor].obtener_sig()
            posicion += 1
        return None

    def siguiente_posicion(self):
        if self.__cursor != -1:
            siguiente_celda = self.__espacio[self.__cursor].obtener_sig()
            if siguiente_celda != -1:
                self.__cursor = siguiente_celda

    def anterior_posicion(self):
        if self.__cursor != -1:
            if self.__inicio == self.__cursor:
                self.__cursor = -1
            else:
                cursor = self.__inicio
                anterior_celda = -1
                while cursor != -1 and cursor != self.__cursor:
                    anterior_celda = cursor
                    cursor = self.__espacio[cursor].obtener_sig()
                if anterior_celda != -1:
                    self.__cursor = anterior_celda

    def recorrer(self):
        elementos = []
        cursor = self.__inicio
        while cursor != -1:
            elementos.append(self.__espacio[cursor].obtener_item())
            cursor = self.__espacio[cursor].obtener_sig()
        return elementos

    def obtener_celda_libre(self):
        for i in range(len(self.__espacio)):
            if self.__espacio[i].obtener_item() == 0:
                return i
        return -1
    
    def mostrar_espacio(self):
        for i, celda in enumerate(self.__espacio):
            print(f"Celda {i}: item={celda.obtener_item()}, sig={celda.obtener_sig()}")
    
    
max_size = 20

# Ejemplo de uso
mi_lista_enlazada = ListaEnlazadaCursor(max_size)
mi_lista_enlazada.insertar(10)
mi_lista_enlazada.insertar(20)
mi_lista_enlazada.insertar(30)



print("Lista enlazada con cursor actual:")
print(mi_lista_enlazada.recorrer())

print("\nContenido del espacio de celdas:")
mi_lista_enlazada.mostrar_espacio()