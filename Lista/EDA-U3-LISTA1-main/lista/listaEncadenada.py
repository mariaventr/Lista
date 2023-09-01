class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getValor(self):
        return self.__dato
    
    def setSiguiente(self, objeto):
        self.__siguiente=objeto

    def getSiguiente(self):
        return self.__siguiente

class Lista:
    def __init__(self):
        self.cabeza = None

    def Insertar(self, X, p):
        """
        Inserta el elemento X en la posición p de la lista.
        """
        nuevo_nodo = Nodo(X)

        if p == 0:
            nuevo_nodo.setSiguiente(self.cabeza)
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            posicion = 0

            while actual is not None and posicion < p - 1:
                actual = actual.getSiguiente()
                posicion += 1

            if actual is not None:
                nuevo_nodo.setSiguiente(actual.getSiguiente())
                actual.setSiguiente(nuevo_nodo)
            else:
                print("Posición fuera de rango.")

    def Suprimir(self, p):
        """
        Elimina el elemento en la posición p de la lista.
        """
        if p == 0:
            if self.cabeza is not None:
                self.cabeza = self.cabeza.getSiguiente()
            else:
                print("La lista está vacía.")
        else:
            actual = self.cabeza
            anterior = None
            posicion = 0

            while actual is not None and posicion < p:
                anterior = actual
                actual = actual.getSiguiente()
                posicion += 1

            if actual is not None:
                anterior.setSiguiente(actual.getSiguiente())
            else:
                print("Posición fuera de rango.")

    def Recuperar(self, p):
        """
        Recupera el elemento en la posición p de la lista.
        """
        actual = self.cabeza
        posicion = 0

        while actual is not None and posicion < p:
            actual = actual.getSiguiente()
            posicion += 1

        if actual is not None:
            return actual.getValor()
        else:
            print("Posición fuera de rango.")
            return None

    def Buscar(self, X):
        """
        Busca el elemento X en la lista y devuelve su posición si se encuentra, o -1 si no se encuentra.
        """
        actual = self.cabeza
        posicion = 0

        while actual is not None:
            if actual.getValor() == X:
                return posicion
            actual = actual.getSiguiente()
            posicion += 1

        return -1

    def Primer_elemento(self):
        """
        Devuelve el primer elemento de la lista.
        """
        if self.cabeza is not None:
            return self.cabeza.getValor()
        else:
            print("La lista está vacía.")
            return None

    def Ultimo_elemento(self):
        """
        Devuelve el último elemento de la lista.
        """
        actual = self.cabeza

        while actual is not None and actual.getSiguiente() is not None:
            actual = actual.getSiguiente()

        if actual is not None:
            return actual.getValor()
        else:
            print("La lista está vacía.")
            return None

    def Siguiente(self, p):
        """
        Devuelve la posición del elemento siguiente a la posición p en la lista.
        """
        actual = self.cabeza
        posicion = 0

        while actual is not None and posicion < p:
            actual = actual.getSiguiente()
            posicion += 1

        if actual is not None and actual.getSiguiente() is not None:
            return posicion + 1
        else:
            print("Posición fuera de rango.")
            return None

    def Anterior(self, p):
        """
        Devuelve la posición del elemento anterior a la posición p en la lista.
        """
        if p == 0:
            print("Posición fuera de rango.")
            return None
        elif p == 1:
            return 0
        else:
            actual = self.cabeza
            anterior = None
            posicion = 0

            while actual is not None and posicion < p:
                anterior = actual
                actual = actual.getSiguiente()
                posicion += 1

            if actual is not None:
                return posicion - 1
            else:
                print("Posición fuera de rango.")
                return None

    def Recorrer(self):
        """
        Imprime todos los elementos de la lista.
        """
        actual = self.cabeza

        while actual is not None:
            print(actual.getValor())
            actual = actual.getSiguiente()

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