import numpy as np
from ColaEncadena import ColaEncadenada
class GrafoSecuencial:
    __cantVertices = None
    __matrizAdyacencia = None

    def __init__(self,cantVertices) -> None:
        self.__cantVertices = cantVertices
        self.__matrizAdyacencia = np.zeros((cantVertices,cantVertices),dtype= int)
    
    def CrearArco(self,vertice1,vertice2):
        if vertice1 >= self.__cantVertices or vertice1 < 0 or vertice2 >= self.__cantVertices or vertice2 < 0:
            print("Vertices no existente")
        else:
            self.__matrizAdyacencia[vertice1,vertice2] = 1
            self.__matrizAdyacencia[vertice2,vertice1] = 1
    
    def mostrarArreglo(self):
        print(self.__matrizAdyacencia)
    
    def esAdyacente(self,vertice1,vertice2):
        if self.__matrizAdyacencia[vertice1,vertice2] == 1 or self.__matrizAdyacencia[vertice2,vertice1] == 1:
            print("Es adyacente")
        else:
            print("No son adyacentes")
    
    def RecorridoEnAnchura(self,origen):
        arreglo = -1*np.ones(self.__cantVertices,dtype=int)
        cola = ColaEncadenada()

        cola.Insertar(origen)
        arreglo[origen] = 0
        v = 0
        while not cola.vacia():
            cola.Suprimir()
            for i in range(self.__cantVertices):
                if self.__matrizAdyacencia[v,i] == 1:
                    if arreglo[i] == -1:
                        arreglo[i] = arreglo[v] + 1
                        cola.Insertar(i)
            v+=1
        print(arreglo)
    
    def

    def REP(self):
        arreglo = np.zeros()
        tiempo = 0
        for i in range(self.__cantVertices):
            if arreglo[i] == 0:
                self.REPvisita()
    
    def REPvisita(self,s,tiempo):
        pass


