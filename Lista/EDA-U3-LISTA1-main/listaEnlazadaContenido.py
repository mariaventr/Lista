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

class ListaPorContenido:
    def __init__(self):
        self.__cabeza = None

    def Insertar(self, X):
        nuevo_nodo = Nodo(X)
        if self.Buscar(X) == -1:
            nuevo_nodo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo_nodo

    def Suprimir(self, X):
        actual = self.__cabeza
        anterior = None

        while actual is not None:
            if actual.getValor() == X:
                if anterior is None:
                    self.__cabeza = actual.getSiguiente()
                else:
                    anterior.setSiguiente(actual.getSiguiente())
                return
            anterior = actual
            actual = actual.getSiguiente()

    def Buscar(self, X):
        actual = self.__cabeza
        posicion = 0

        while actual is not None:
            if actual.getValor() == X:
                return posicion
            actual = actual.getSiguiente()
            posicion += 1

        return -1

    def Recorrer(self):
        actual = self.__cabeza

        while actual is not None:
            print(actual.getValor())
            actual = actual.getSiguiente()

lista = ListaPorContenido()
lista.Insertar(10)
lista.Insertar(20)
lista.Insertar(30)
lista.Recorrer()  

print("Despues del suprimir")
lista.Suprimir(20)
lista.Recorrer()  

print("Buscar")
print(lista.Buscar(10)) 