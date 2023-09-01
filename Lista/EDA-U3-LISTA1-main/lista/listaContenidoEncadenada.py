class NodoPorContenido:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None

class ListaEncadenadaPorContenido:
    def __init__(self):
        self.inicio = None

    def insertar(self, elemento):
        nuevo_nodo = NodoPorContenido(elemento)
        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            cursor = self.inicio
            while cursor.siguiente is not None:
                cursor = cursor.siguiente
            cursor.siguiente = nuevo_nodo

    def suprimir(self, elemento):
        if self.inicio is None:
            return None
        if self.inicio.elemento == elemento:
            elemento_eliminado = self.inicio.elemento
            self.inicio = self.inicio.siguiente
            return elemento_eliminado
        cursor = self.inicio
        while cursor.siguiente is not None:
            if cursor.siguiente.elemento == elemento:
                elemento_eliminado = cursor.siguiente.elemento
                cursor.siguiente = cursor.siguiente.siguiente
                return elemento_eliminado
            cursor = cursor.siguiente
        return None

    def recuperar(self, posicion):
        cursor = self.inicio
        posicion_actual = 1
        while cursor is not None and posicion_actual < posicion:
            cursor = cursor.siguiente
            posicion_actual += 1
        if cursor is not None:
            return cursor.elemento
        else:
            return None

    def buscar(self, elemento):
        cursor = self.inicio
        posicion = 1
        while cursor is not None:
            if cursor.elemento == elemento:
                return posicion
            cursor = cursor.siguiente
            posicion += 1
        return None

    def primer_elemento(self):
        if self.inicio is not None:
            return self.inicio.elemento
        else:
            return None

    def ultimo_elemento(self):
        cursor = self.inicio
        if cursor is None:
            return None
        while cursor.siguiente is not None:
            cursor = cursor.siguiente
        return cursor.elemento

    def siguiente_elemento(self, elemento):
        cursor = self.inicio
        while cursor is not None:
            if cursor.elemento == elemento and cursor.siguiente is not None:
                return cursor.siguiente.elemento
            cursor = cursor.siguiente
        return None

    def anterior_elemento(self, elemento):
        if self.inicio is None or self.inicio.elemento == elemento:
            return None
        cursor = self.inicio
        while cursor.siguiente is not None:
            if cursor.siguiente.elemento == elemento:
                return cursor.elemento
            cursor = cursor.siguiente
        return None

    def recorrer(self):
        elementos = []
        cursor = self.inicio
        while cursor is not None:
            elementos.append(cursor.elemento)
            cursor = cursor.siguiente
        return elementos
    
mi_lista_secuencial_por_contenido = ListaEncadenadaPorContenido()
mi_lista_secuencial_por_contenido.insertar(10)
mi_lista_secuencial_por_contenido.insertar(20)
mi_lista_secuencial_por_contenido.insertar(30)
print("Lista secuencial por contenido actual:", mi_lista_secuencial_por_contenido.recorrer())
mi_lista_secuencial_por_contenido.suprimir(20)
print("Despues Suprimir:", mi_lista_secuencial_por_contenido.recorrer())