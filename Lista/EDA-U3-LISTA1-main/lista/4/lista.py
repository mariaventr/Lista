import numpy as np
import csv
from Designacion import designacion

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

    def cargarArchivo(self):
        archivo=open("designacion.csv", encoding='utf-8')
        reader = csv.reader(archivo, delimiter=',')
        next(reader)
        for row in reader:
            anio=row[0]
            cargo=row[1].lower()
            instancia=row[2].lower()
            materia=row[3].lower()
            mujeres = int(row[5])
            varones = int(row[4])
            objeto=designacion(anio, cargo, instancia, materia, mujeres, varones)
            self.insertar(objeto)

    def cargoPorAño(self):
        cargo=input("Ingresar tipo de cargo: ")
        dicc={}
        for objeto in self.lista:
            if objeto.getCargo()==cargo:
                if objeto.getAnio() not in dicc:
                    dicc[objeto.getAnio()]=objeto.getMujeres()
                else:
                    dicc[objeto.getAnio()]+=objeto.getMujeres()

        for anio, mujeres in dicc.items():
            print(f"Año: {anio}, Cantidad de Mujeres en {cargo}: {mujeres}")
    
    def agentes(self):
        cargo=input("Ingresar tipo de cargo: ")
        materia=input("Ingresar tipo de materia: ")
        anio=input("Ingresar año: ")
        total=0
        for objeto in self.lista:
            if objeto.getCargo()==cargo and objeto.getMateria()==materia and objeto.getAnio()==anio:
                total+=objeto.getMujeres()+objeto.getVarones()
        print(f"Para el Cargo: {cargo}, Materia: {materia}, Año: {anio} existen: {total} agentes")


if __name__=="__main__":
    lista=ListaSecuencialPorContenido()
    lista.cargarArchivo()
    lista.cargoPorAño()
    lista.agentes()