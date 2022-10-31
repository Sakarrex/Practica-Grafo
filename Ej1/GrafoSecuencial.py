
import numpy as np

from ColaEncadena import ColaEncadenada
from CeldaTabla import CeldaTabla
class GrafoSecuencial:
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
            self.__matrizAdyacencia[vertice2,vertice1] = peso
    
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

    
   
    
    def Conexo(self):
        band = True
        i = 0
        while i < self.__cantVertices and band:
            if len(self.Adyacentes(i)) == 0:
                band = False
            i+=1
        if band == False:
            print("Es disconexo")
        else:
            print("Es conexo")


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




    def REP(self, actual,arreglo = None, recorrido = None):
            if actual >=0  and actual < self.__cantVertices:
                arreglo = np.zeros(self.__cantVertices,dtype = int)
                recorrido = []
                recorrido = self.REP_visita(actual = actual , arreglo = arreglo,recorrido = recorrido)
                return recorrido
            else:
                print('ERROR: vertice  origen no valido')
                return None
            
        
    
    def REP_visita(self,actual,arreglo,recorrido):
        recorrido.append(actual)
        arreglo[actual] = 1
        adyacentes = self.Adyacentes(actual)
        for adyacente in adyacentes:
            if arreglo[adyacente] == 0:
               recorrido =  self.REP_visita(adyacente ,arreglo = arreglo,recorrido = recorrido)

         
        return recorrido
    
    def Aciclico(self,actual,arreglo,recorrido,ciclico):
        if not ciclico:
            recorrido.append(actual)
            arreglo[actual] = 1
            adyacentes = self.Adyacentes(actual)
            for adyacente in adyacentes:
                if arreglo[adyacente] == 0:
                    ciclico =  self.C(adyacente ,arreglo = arreglo,recorrido = recorrido,ciclico=ciclico)
                elif len(recorrido) >= 3:
                    ciclico = True
         
        return ciclico


