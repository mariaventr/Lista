class designacion:
    def __init__(self, anio, cargo, instancia, materia, mujeres, varones):
        self.__anio = anio
        self.__cargo = cargo
        self.__instancia = instancia
        self.__materia = materia
        self.__cant_mujeres = mujeres
        self.__cant_varones = varones


    def getAnio(self):
        return self.__anio


    def getCargo(self):
        return self.__cargo


    def getMateria(self):
        return self.__materia


    def getMujeres(self):
        return self.__cant_mujeres


    def getVarones(self):
        return self.__cant_varones


    

    
