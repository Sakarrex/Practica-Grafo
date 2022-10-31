
import numpy as np

from ColaEncadena import ColaEncadenada
from CeldaTabla import CeldaTabla
class DigrafoSecuencial:
    __cantVertices = None
    __matrizAdyacencia = None

    def __init__(self,cantVertices) -> None:
        self.__cantVertices = cantVertices
        self.__matrizAdyacencia = np.zeros((cantVertices,cantVertices),dtype= int)
    
    def CrearArco(self,vertice1,vertice2,peso = 1):
        if vertice1 >= self.__cantVertices or vertice1 < 0 or vertice2 >= self.__cantVertices or vertice2 < 0:
            print("Vertices no existente")
        else:
            self.__matrizAdyacencia[vertice1,vertice2] = peso
            
    
    def mostrarArreglo(self):
        print(self.__matrizAdyacencia)
    
    def Adyacentes(self,vertice):
        adyacentes = []
        for i in range(self.__cantVertices):
            if self.__matrizAdyacencia[vertice,i]:
                adyacentes.append(i)
        return adyacentes
    
    def getCamino(self,inicio,fin):
        d= np.zeros(self.__cantVertices,dtype=int)
        resultado = self.REP_visita(inicio, fin, d)
        if isinstance(resultado,list):
            resultado.insert(0,inicio)
        return resultado
    
    def REP_visita(self, nodo_origen, nodo_destino, d):
        d[nodo_origen] = 1
        adys = self.Adyacentes(nodo_origen)
        for nodos in adys:
            if nodos == nodo_destino:
                return [nodo_destino]
            if d[nodos] == 0:
                retorno = self.REP_visita(nodos, nodo_destino, d)
                if isinstance(retorno, list):
                    retorno.insert(0,nodos)
                    return retorno
        return 0

    
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
                
                if i != j and matriz[i,j] == 0:
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
            for i in self.Adyacentes(v):
                    if arreglo[i] == -1:
                        arreglo[i] = arreglo[v] + 1
                        cola.Insertar(i)
            v+=1
        print(arreglo)
    
    def Dijkstra(self,origen,destino):
        Tabla = np.empty(self.__cantVertices,dtype=CeldaTabla)
        for i in range(self.__cantVertices):
            Tabla[i] = CeldaTabla()
        Tabla[origen].setDistancia(0)
        v = origen
        for i in range(self.__cantVertices):
            v = self.getV(Tabla)
            Tabla[v].setConocido(True)
            for w in self.Adyacentes(v):
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

    
    def Prim(self,origen):
        Tabla = np.empty(self.__cantVertices,dtype=CeldaTabla)

        for i in range(self.__cantVertices):
            Tabla[i] = CeldaTabla()

        Tabla[origen].setDistancia(0)
        v = origen

        for i in range(self.__cantVertices):
            v = self.getV(Tabla)
            Tabla[v].setConocido(True)
            for w in self.Adyacentes(v):
                if self.__matrizAdyacencia[v,w] == 1:
                    if Tabla[w].getConocido() == False:
                        if self.__matrizAdyacencia[v,w] < Tabla[w].getDistancia():
                            Tabla[w].setDistancia(self.__matrizAdyacencia[v,w])
                            Tabla[w].setCamino(v)
        for i in range(len(Tabla)):
            print(str(i) + ": " + str(Tabla[i]))

    

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
        for s in range(self.__cantVertices):
            if arreglo[s] == 0:
                arreglo = self.REPvisita(arreglo,s,tiempo)
        print(arreglo)
    
    def REPvisita(self,arreglo,s,tiempo):
        tiempo +=1
        arreglo[s] = tiempo
        for u in self.Adyacentes(s):
            if arreglo[u] == 0:
                return self.REPvisita(arreglo,u,tiempo)
        tiempo +=1
        return arreglo


