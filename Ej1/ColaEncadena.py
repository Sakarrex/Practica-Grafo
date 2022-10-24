from NodoCola import NodoCola

class ColaEncadenada:
    __cabeza = None
    __ultimo = None

    def __init__(self) -> None:
        self.__cabeza = None
        self.__ultimo = self.__cabeza
    
    def vacia(self):
        return self.__cabeza == None
    
    def Insertar(self,valor):
        nuevoNodo = NodoCola(valor)
        if self.vacia():
            self.__cabeza = nuevoNodo
            self.__ultimo = nuevoNodo
        else:
            self.__ultimo.setSiguiente(nuevoNodo)
            self.__ultimo = nuevoNodo
    
    def Suprimir(self):
        valorDevolver=None
        if not self.vacia():
            valorDevolver = self.__cabeza.getValor()
            self.__cabeza = self.__cabeza.getSiguiente()
        else:
            print("Cola vacia no se puede suprimir")
        return valorDevolver
    
    def recorrer(self):
        aux = self.__cabeza
        i = 1
        while aux != None:
            print(str(i) +": " + str(aux.getValor()))
            aux = aux.getSiguiente()
            i += 1