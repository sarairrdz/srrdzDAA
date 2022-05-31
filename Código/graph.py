"""
Proyecto 1 - Biblioteca de generación y manejo de grafos
Diseño y Análisis de algoritmos
Semestre A22

Alumna: Saraí Roque Rodríguez

"""

### Clase Grafo --  Graph Class ###


from node import Node
from edge import Edge
import random


class Graph:
    def __init__(self):  # Constructor
        self.nodes = {}  # Nodos del grafo    -- Graph Nodes
        self.edges = {}  # Aristas del grafo  -- Graph Edges
        self.attr = {}  
        self.type = None  # Tipo de grafo   -- Type of graph

    def addNode(self, name):
        """
       Agregar nodo al grafo -- Add node to graph
       :param name: Nombre del nodo -- Name of the node
       :return: El nodo se encontró o fue creado  -- The node was found or created
        """

        nodo = self.nodes.get(name)  # Verificar que el nodo no se ha creado
        if nodo is None:  # Si el nodo no se ha creado
            
            nodo = Node(name)
            #Agregar a diccionario de nodos de grafo
            self.nodes[name] = nodo
        # else:
        #     print("El nodo ya existe ")

        return nodo

    def addEdge(self, source, target,label):
        """
        Agregar una arista al grafo -- Add edge to graph
        :param label: Etiqueta de arista -- Label asinged to edge "{source} -> {target}"
        :param souce: Nodo origen -- Source node
        :param target: Nodo destino -- Target node
        :return: Arista se encontró o fue creada -- The node was found or created
        """
        #Verificar que la arista no se ha creado
        ed = self.edges.get(label)
        if ed is None:
            #Crear los nodos si no existen
            s = self.addNode(source)
            t = self.addNode(target)
            #Crear Arista
            # print("Crear arista", label)
            ed = Edge( s, t, label)

            #Agregar a diccionario de Aristas del grafo
            self.edges[label] = ed  # edge

            #Atributos de la arista
            s.attr["NEIGHBORS"].append(t)
            s.attr["EDGES"].append(ed)
            t.attr["NEIGHBORS"].append(s)
            t.attr["EDGES"].append(ed)
        # else:
        #     print("La arista  ya existe ")
        return ed

    def getNodes(self):
        """
        Regresa una lista de nodos en el grafo -- Return list of nodes of graph
        :return: lista de nodos si existen -- list of nodes in graph
        """
        return list(self.nodes.keys())

    def getEdges(self):
        """
        Regresa una lista de aristas en el grafo -- Return list of edges of graph
        """
        graph_Edges = []
        for edge in self.edges.values():
            graph_Edges.append([edge.source.id, edge.target.id])
        return graph_Edges
    
    def getType(self):
        """
        Regresa el tipo de generador usado en el  grafo  --  Returns the type of graph generated
        :return: tipo de grafo correspondiente  -- type of graph
        """

        graph_Type = ["GRID","ERDOS-RENYI","GILBERT","GEOGRAPHIC_SIMPLE","BARABASI-ALBERT","DOROGOVRSEV-MENDES"]

        return graph_Type[self.type]

