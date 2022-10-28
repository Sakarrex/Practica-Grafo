import numpy as np

from Nodo import Nodo
class GrafoEncadenado:
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
            self.InsertarArreglo(nodo2,nodo1)
    
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
    
    def Mostrar(self):
        for i in range(len(self.__arreglo)):
            cadena = str(i) + ": "
            aux = self.__arreglo[i]
            while aux != None:
                cadena += str(aux.getValor())
                aux = aux.getSiguiente()
            print(cadena)
