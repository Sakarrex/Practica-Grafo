from DigrafoSecuencial import DigrafoSecuencial

if __name__ == '__main__':
    UnGrafo = DigrafoSecuencial()
    UnGrafo.CrearArco("A","B")
    UnGrafo.CrearArco("A","D")
    UnGrafo.CrearArco("B","C")
    UnGrafo.CrearArco("B","E")
    UnGrafo.CrearArco("B","F")
    UnGrafo.CrearArco("C","D")
    UnGrafo.CrearArco("D","B")
    UnGrafo.CrearArco("E","D")
    UnGrafo.CrearArco("E","F")
    UnGrafo.CrearArco("F","A")
    UnGrafo.CrearArco("F","D")

    UnGrafo.Djikstra("A","F")
