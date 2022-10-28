from DigrafoSecuencial import DigrafoSecuencial

if __name__ == '__main__':
    UnGrafo = DigrafoSecuencial()
    UnGrafo.CrearArco("A","B",3)
    UnGrafo.CrearArco("A","D",6)
    UnGrafo.CrearArco("B","C",1)
    UnGrafo.CrearArco("B","E",2)
    UnGrafo.CrearArco("B","F",1)
    UnGrafo.CrearArco("C","D",2)
    UnGrafo.CrearArco("D","B",3)
    UnGrafo.CrearArco("E","D",3)
    UnGrafo.CrearArco("E","F",2)
    UnGrafo.CrearArco("F","A",5)
    UnGrafo.CrearArco("F","D",1)

    UnGrafo.Djikstra("B","D")
