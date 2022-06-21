"""
Proyecto 2 - Algoritmos BSF y DFS
Diseño y Análisis de algoritmos
Semestre A22
Alumna: Saraí Roque Rodríguez

"""

### Clase Grafo --  Graph Class ###


from node import Node
from edge import Edge
import random

BFS_TREE = 6
DFS_R_TREE = 7
DFS_I_TREE = 8
GENERATOR_NONE=100


class Graph:
    def __init__(self):  # Constructor
        self.nodes = {}  # Nodos del grafo    -- Graph Nodes
        self.edges = {}  # Aristas del grafo  -- Graph Edges
        self.attr = {}  
        self.type = None  # Tipo de grafo   -- Type of graph
        self.generator=None #Generador

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

        graph_Type = ["GRID","ERDOS-RENYI","GILBERT","GEOGRAPHIC_SIMPLE","BARABASI-ALBERT","DOROGOVRSEV-MENDES","BFS_TREE","DFS_R_TREE","DFS_I_TREE"]

        return graph_Type[self.type]
    
    def getGenerator(self):
        """
        Regresa el generador de su origen
        """
        if self.generator is None:
            return ""
        if self.generator ==100:
            return ""
        else:
            graph_Generator_Type = ["GRID","ERDOS-RENYI","GILBERT","GEOGRAPHIC_SIMPLE","BARABASI-ALBERT","DOROGOVRSEV-MENDES","BFS_TREE","DFS_R_TREE","DFS_I_TREE"]
            return graph_Generator_Type[self.generator]

    def BFS(self,s):
        """
        Genera un árbol con el Algoritmo Búsqueda a lo Ancho (Breadth First Search) BFS
        :param s: Nodo fuente del árbol 
        :return: Árbol BFS -- BFS tree
        """
        #Crear árbol con objeto tipo Grafo y asignar tipo árbol
        tree = Graph()
        tree.type = BFS_TREE
        tree.generator=self.type
        
        #Agregar nodo fuente
        tree.addNode(s)

        #Lista de Nodos Visitados 
        visited = [False] * (len(self.nodes.keys())+1)
        visited[s] = True
       
        # Lista de capas del árbol
        L = []
        Ls = []
        L.append(s)
        Ls.append([s])
        # Pasar por todos los nodos del grafo
        while L:
            # Se obtienen vecinos del nodo s y se crean aristas si el nodo vecino no ha sido visitado
            s = L.pop(0)
            vecinos = self.nodes[s].attr['NEIGHBORS']
            L_i = []
            for vecino in vecinos:
                if visited[vecino.id] == False:
                    L.append(vecino.id)
                    visited[vecino.id] = True
                    tree.addEdge(s, vecino.id, f"{s}--{vecino.id}")
                    L_i.append(vecino.id)
            # También se guardan las capas del árbol
            if len(L_i) > 0:
                Ls.append(L_i)

        return tree, Ls


    def DFS_AUX(self,s,tree,visited):
        """
        Función de para llamada recursiva del algoritmo DFS
        :param s: Nodo fuente
        :param tree: Árbol DFS
        :param visited: conjunto de  nodos visitados
        :return tree: Árbol DFS estado recursivo
        """
        #Agregar nodo fuente a visitados
        visited.add(s)
        
        #Vecinos de nodo
        vecinos = self.nodes[s].attr['NEIGHBORS']

        for vecino in vecinos:
            # Si el vecino no ha sido visitado se crea arista 
            if vecino.id not in visited:
                tree.addEdge(s, vecino.id, f'{s}->{vecino.id}')
                #Llamada recursiva a la función, con nodo vecino ahora como nodo fuente
                self.DFS_AUX(vecino.id, tree, visited)
        return tree

    def DFS_R(self,s):
        """
        Algoritmo de Búsqueda en profundidad Recursivo (Depth First Search) DFS-R
        :param: Nodo fuente 
        :return: Árbol DFS
        """
        #Crear árbol con objeto tipo Grafo y asignar tipo árbol
        tree = Graph()
        tree.type = DFS_R_TREE
        tree.generator=self.type

        #Conjunto de nodos visitados
        visited = set()

        #Llamada de DFS Recursivo
        t_DFSR=self.DFS_AUX(s,tree,visited)
        return t_DFSR

    def DFS_I(self,s):
        """
        Algoritmo de Búsqueda en profundidad Iterativo (Depth First Search) DFS-I
        :param: Nodo fuente 
        :return: Árbol DFS
        """   
        #Crear árbol con objeto tipo Grafo y asignar tipo árbol
        tree = Graph()
        tree.type = DFS_I_TREE
        tree.generator=self.type

        #Nodos explorados inicia con nodo fuente
        discovered = [s]
        u = s
        #Stack para DFS
        stack = []

        #Mientras stack tenga elementos 
        while True:
            #Vecinos del nodo u
            vecinos =  self.nodes[u].attr['NEIGHBORS']
            #Para cada vecino del nodo u
            for vecino in vecinos:
                #Si el vecino no ha sido descubierto
                if vecino.id not in discovered:
                    #Agregar al stack
                    stack.append(vecino.id)

            #Si el stack está vacío terminar el ciclo
            if not stack:
                break
            
            #Extraer el útimo elemento del stack
            # Hasta que el nodo c sale de la stack se agrega a los nodos descuviertos
            p, c = u, stack.pop()
                # Si el nodo c no ha sido visitado se crea arista de p a c (p->c)
                # y se marca como descubierto. 
            if c not in discovered:
                tree.addEdge(p, c, f"{p}->{c}")
                discovered.append(c)
                # se actualiza el nodo fuente u = c 
                u = c
            
        return tree