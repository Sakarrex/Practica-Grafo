class NodoCola:
    __valor = 0
    __siguiente = None

    def __init__(self,valor):
        self.__valor = valor
        self.__siguiente = None
    
    def getValor(self):
        return self.__valor
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente