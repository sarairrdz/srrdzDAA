"""
Proyecto 3 - Algoritmo de Dijkstra
Diseño y Análisis de algoritmos
Semestre A22

Alumna: Saraí Roque Rodríguez

"""

### Clase Arista -- Edge Class ###


class Edge:
    def __init__(self, source,target,label):
        self.label  = label
        self.source = source
        self.target = target
        self.atrr   = {}
        