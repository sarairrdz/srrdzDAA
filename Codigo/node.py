"""
Proyecto 3 - Algoritmo de Dijkstra
Diseño y Análisis de algoritmos
Semestre A22

Alumna: Saraí Roque Rodríguez

"""

### Clase Nodo --  Graph Node Class ###

import numpy as np
import random 



class Node:
    def __init__(self, id):
        self.id = id
        self.attr = {
            "EDGES": [],
            "NEIGHBORS": [],
            "POS": np.array([random.random(),random.random()]) #Posición aleatoria al Nodo
        }
        self.attr["DEGREE"]=len(self.attr["NEIGHBORS"]) #Grado del nodo

