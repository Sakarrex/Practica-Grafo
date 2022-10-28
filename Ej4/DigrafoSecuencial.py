import numpy as np
import sys
from CeldaTabla import CeldaTabla
class DigrafoSecuencial:
    __cantVertices = None
    __matrizAdyacencia = None
    __diccionario = None

    def __init__(self,cantVertices=6) -> None:
        self.__cantVertices = cantVertices
        self.__matrizAdyacencia = np.zeros((cantVertices,cantVertices),dtype= int)
        self.__diccionario = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}

    def CrearArco(self,vertice1,vertice2,peso):
        if vertice1 not in self.__diccionario or vertice2 not in self.__diccionario:
            print("Vertices no existente")
        else:
            self.__matrizAdyacencia[self.__diccionario[vertice1],self.__diccionario[vertice2]] = peso
        
    
    
    
    
    def Djikstra(self,origen,destino):
        Tabla = np.empty(self.__cantVertices,dtype=CeldaTabla)
        for i in range(self.__cantVertices):
            Tabla[i] = CeldaTabla()
        v = self.__diccionario[origen]
        Tabla[v].setDistancia(0)
        for i in range(self.__cantVertices):
            v = self.getV(Tabla)
            Tabla[v].setConocido(True)
            for w in range(self.__cantVertices):
                if self.__matrizAdyacencia[v,w] != 0:
                    if Tabla[w].getConocido() == False:
                        if (Tabla[v].getDistancia() + self.__matrizAdyacencia[v,w]) < Tabla[w].getDistancia():
                            Tabla[w].setDistancia(Tabla[v].getDistancia() + self.__matrizAdyacencia[v,w])
                            Tabla[w].setCamino(v)
                
        keys = list(self.__diccionario)
        v = self.__diccionario[destino]
        camino = [keys[v]]
        
        while Tabla[v].getCamino() != None:
            v = Tabla[v].getCamino()
            camino.insert(0,keys[v])
        print(camino)
    
    def getV(self,Tabla):
        v = 0
        mindist = sys.maxsize
        for i in range(len(Tabla)):
            if Tabla[i].getConocido() == False and Tabla[i].getDistancia() < mindist:
                v = i
                mindist = Tabla[i].getDistancia()
        return v

    def mostrarArreglo(self):
        print(self.__matrizAdyacencia)