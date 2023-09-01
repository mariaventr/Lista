from Designacion import designacion
import csv

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
    
class Designacion:
    def __init__(self, anio, cargo, instancia, materia, mujeres, varones):
        self.anio = anio
        self.cargo = cargo
        self.instancia = instancia
        self.materia = materia
        self.mujeres = mujeres
        self.varones = varones

def leer_datos_csv(nombre_archivo):
    lista_designaciones = ListaEncadenadaPorContenido()
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv, None)
        for fila in lector_csv:
            anio, cargo, instancia, materia, mujeres, varones = fila
            designacion_obj = Designacion(int(anio), cargo, instancia, materia, int(mujeres), int(varones))
            lista_designaciones.insertar(designacion_obj)
    return lista_designaciones

def cantidad_mujeres_por_cargo_y_anio(lista_designaciones, cargo_buscado):
    dicc = {}
    cursor = lista_designaciones.inicio
    while cursor is not None:
        designacion_obj = cursor.elemento
        if designacion_obj.cargo == cargo_buscado:
            if designacion_obj.anio not in dicc:
                dicc[designacion_obj.anio] = designacion_obj.mujeres
            else:
                dicc[designacion_obj.anio] += designacion_obj.mujeres
        cursor = cursor.siguiente

    for anio, mujeres in dicc.items():
        print(f"Año: {anio}, Cantidad de Mujeres en {cargo_buscado}: {mujeres}")

if __name__ == "__main__":
    nombre_archivo = "designacion.csv"  # Reemplaza con el nombre de tu archivo CSV
    lista_designaciones = leer_datos_csv(nombre_archivo)

    cargo_buscado = input("Ingresar tipo de cargo: ")
    cantidad_mujeres_por_cargo_y_anio(lista_designaciones, cargo_buscado)
   