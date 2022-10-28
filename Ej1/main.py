from GrafoSecuencial import GrafoSecuencial
from GrafoEncadenado import GrafoEncadenado
if __name__ == "__main__":
    UnGrafo = GrafoSecuencial(6)
    UnGrafo.CrearArco(0,1)
    UnGrafo.CrearArco(0,2)
    UnGrafo.CrearArco(1,3)
    UnGrafo.CrearArco(1,4)
    UnGrafo.CrearArco(3,4)
    
    UnGrafo.Djikstra(0,4)
