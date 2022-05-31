"""
Proyecto 1 - Biblioteca de generación y manejo de grafos
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
        
