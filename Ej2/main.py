from DigrafoSecuencial import DigrafoSecuencial
from DigrafoEncadenado import DigrafoEncadenado
if __name__ == "__main__":
    UnGrafo = DigrafoEncadenado(4)
    UnGrafo.CrearArco(0,1)
    UnGrafo.CrearArco(0,2)
    UnGrafo.CrearArco(2,3)
    UnGrafo.CrearArco(3,1)
    
    
    print(UnGrafo.WARSHALL())
