import numpy as np
from ColaEncadena import ColaEncadenada
from Ej4.CeldaTabla import CeldaTabla
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
    
    def Adyacentes(self,vertice):
        for i in range(self.__cantVertices):
            if self.__matrizAdyacencia[vertice,i] == 1:
                print(i)
    
    "Camino entre nodos"
    def WARSHALL (self):
        matrizCamino = self.__matrizAdyacencia
        
        for k in range(self.__cantVertices):
            for i in range(self.__cantVertices):
                for j in range(self.__cantVertices):
                    if matrizCamino[i,j]  == 1 or (matrizCamino[i,k] * matrizCamino[k,j]) == 1:
                        matrizCamino[i,j] = 1
                    else:
                        matrizCamino[i,j] = 0
        return matrizCamino
    
    def Conexo(self):
        matriz = self.WARSHALL()
        resultado = True
        i = 0
        while i < self.__cantVertices and resultado:
            j=0
            while j < self.__cantVertices and resultado:
                if matriz[i,j] == 0:
                    resultado = False
                j+=1
            i+=1
        print(resultado)

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
    
    def Djikstra(self,origen,destino):
        Tabla = np.empty(self.__cantVertices,dtype=CeldaTabla)
        for i in range(self.__cantVertices):
            Tabla[i] = CeldaTabla()
        Tabla[origen].setDistancia(0)
        v = origen
        for i in range(self.__cantVertices):
            v = self.getV(Tabla)
            Tabla[v].setConocido(True)
            for w in range(self.__cantVertices):
                if self.__matrizAdyacencia[v,w] == 1:
                    if Tabla[w].getConocido() == False:
                        if (Tabla[v].getDistancia() + self.__matrizAdyacencia[v,w]) < Tabla[w].getDistancia():
                            Tabla[w].setDistancia(Tabla[v].getDistancia() + self.__matrizAdyacencia[v,w])
                            Tabla[w].setCamino(v)
        v = destino
        camino = [v]
        while Tabla[v].getCamino() != None:
            v = Tabla[v].getCamino()
            camino.insert(0,v)
        print(camino)
    
    def getV(self,Tabla):
        v = 0
        mindist = 99999999
        for i in range(len(Tabla)):
            if Tabla[i].getConocido() == False and Tabla[i].getDistancia() < mindist:
                v = i
                mindist = Tabla[i].getDistancia()
        return v

    def REP(self):
        arreglo = np.zeros(self.__cantVertices, dtype=int)
        tiempo = 0
        for i in range(self.__cantVertices):
            if arreglo[i] == 0:
                self.REPvisita()
    
    def REPvisita(self,s,tiempo):
        pass


