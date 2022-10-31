
import numpy as np
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
    
   
    def Adyacentes(self,matriz,vertice):
        adyacentes = []
        for i in range(self.__cantVertices):
            if matriz[vertice,i]:
                adyacentes.append(i)

        return adyacentes
    
     
    def Conexo(self,matriz,nodo):
        band = True
        i = 0
        while i < self.__cantVertices and band:
            if len(self.Adyacentes(matriz,i)) == 0 and i != nodo:
                band = False
            i+=1
        
        return band
        
 

    def getCriticos(self):
        for i in range(self.__cantVertices):
            
            matrizaux = np.copy(self.__matrizAdyacencia)
            matrizaux[i] = 0
            matrizaux[:,i] = 0
            
            if not self.Conexo(matrizaux,i):
                print(str(i) + " es critico.")
    
    
