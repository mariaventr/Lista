class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaConCursor:
    def __init__(self):
        self.primero = None
        self.cursor = None

    def Insertar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.cursor = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cursor.siguiente
            self.cursor.siguiente = nuevo_nodo

    def Suprimir(self):
        if self.cursor is not None:
            actual = self.primero
            anterior = None
            while actual != self.cursor:
                anterior = actual
                actual = actual.siguiente
            if anterior is not None:
                anterior.siguiente = self.cursor.siguiente
            else:
                self.primero = self.cursor.siguiente
            self.cursor = self.cursor.siguiente

    def Avanzar(self):
        if self.cursor is not None and self.cursor.siguiente is not None:
            self.cursor = self.cursor.siguiente

    def Retroceder(self):
        if self.primero is not None and self.cursor != self.primero:
            actual = self.primero
            while actual.siguiente != self.cursor:
                actual = actual.siguiente
            self.cursor = actual

    def Recuperar(self):
        if self.cursor is not None:
            return self.cursor.dato
        else:
            return None

    def Buscar(self, elemento):
        actual = self.primero
        contador = 0
        while actual is not None:
            if actual.dato == elemento:
                return contador
            actual = actual.siguiente
            contador += 1
        return -1

    def Recorrer(self):
        actual = self.primero
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

# Ejemplo de uso
mi_lista = ListaConCursor()
mi_lista.Insertar(1)
mi_lista.Insertar(2)
mi_lista.Insertar(3)

print("Recorrido de la lista:")
mi_lista.Recorrer()

print("Recuperar elemento del cursor:", mi_lista.Recuperar())
mi_lista.Avanzar()
print("Recuperar elemento después de avanzar:", mi_lista.Recuperar())
mi_lista.Retroceder()
print("Recuperar elemento después de retroceder:", mi_lista.Recuperar())