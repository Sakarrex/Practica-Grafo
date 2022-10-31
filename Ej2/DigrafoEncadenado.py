import numpy as np
from CeldaTabla import CeldaTabla
from Nodo import Nodo
from ColaEncadena import ColaEncadenada
class DigrafoEncadenado:
    __cantVertices = None
    __arreglo = None

    def __init__(self,cantVertices) -> None:
        self.__cantVertices = cantVertices
        self.__arreglo = np.empty(cantVertices,dtype=Nodo)
    
    def CrearArco(self,nodo1,nodo2):
        if nodo1 < 0 or nodo1 >=len(self.__arreglo) or nodo2 < 0 or nodo2 >=len(self.__arreglo):
            print("Nodo no validos")
        else:
            self.InsertarArreglo(nodo1,nodo2)
            
    
    def InsertarArreglo(self,pos,valor):
        NuevoNodo = Nodo(valor)
        if self.__arreglo[pos] == None:
            self.__arreglo[pos] = NuevoNodo
        else:
            aux = self.__arreglo[pos]
            repetido = False
            while aux.getSiguiente() != None and not repetido:
                if aux.getSiguiente().getValor() == valor:
                    repetido = True
                aux = aux.getSiguiente()
            if not repetido:
                aux.setSiguiente(NuevoNodo)
    
    def Adyacentes(self,nodo):
        lista = []
        aux = self.__arreglo[nodo]
        while aux != None:
            lista.append(aux.getValor())
            aux = aux.getSiguiente()
        return lista
    
    def Mostrar(self):
        for i in range(len(self.__arreglo)):
            cadena = str(i) + ": "
            aux = self.__arreglo[i]
            while aux != None:
                cadena += str(aux.getValor())
                aux = aux.getSiguiente()
            print(cadena)
    
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
        return Tabla

    

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

    def WARSHALL (self):
        matrizCamino = np.zeros((self.__cantVertices,self.__cantVertices),dtype=int)
        for i in range(self.__cantVertices):
            for j in self.Adyacentes(i):
                matrizCamino[i,j] = 1
        
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

