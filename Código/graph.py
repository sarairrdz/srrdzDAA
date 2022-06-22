"""
Proyecto 4 - Algoritmos de Kruskal y Prim
Diseño y Análisis de algoritmos
Semestre A22
Alumna: Saraí Roque Rodríguez

"""

### Clase Grafo --  Graph Class ###


from node import Node
from edge import Edge
import random
import numpy as np

BFS_TREE = 6
DFS_R_TREE = 7
DFS_I_TREE = 8
DIJKSTRA_TREE=9
KRUSKALL_D=10
KRUSKALL_I=11
PRIM=12
GENERATOR_NONE=100


class Graph:
    def __init__(self):  # Constructor
        self.nodes = {}  # Nodos del grafo    -- Graph Nodes
        self.edges = {}  # Aristas del grafo  -- Graph Edges
        self.attr = {}  
        self.type = None  # Tipo de grafo   -- Type of graph
        self.generator=None #Generador
        self.ds = []   # Distancias minimas (dijkstra)
        self.mst = 0  # Valor MST

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

        graph_Type = ["GRID","ERDOS-RENYI","GILBERT","GEOGRAPHIC_SIMPLE","BARABASI-ALBERT","DOROGOVRSEV-MENDES","BFS_TREE","DFS_R_TREE","DFS_I_TREE","DIJKSTRA_TREE","KRUSKALL_D","KRUSKALL_I","PRIM"]

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
            graph_Generator_Type = ["GRID","ERDOS-RENYI","GILBERT","GEOGRAPHIC_SIMPLE","BARABASI-ALBERT","DOROGOVRSEV-MENDES","BFS_TREE","DFS_R_TREE","DFS_I_TREE","DIJKSTRA_TREE","KRUSKALL_D","KRUSKALL_I","PRIM"]
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
                    tree.addEdge(s, vecino.id, f"{s}->{vecino.id}")
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
    
    def addDistances(self, rangeL=2, rangeR=50):
        """
        Create a list of random integer numbers for each edge of random graph.
        :param rangeL: left limit (int). Default 2.
        :param rangeR: right limit (int). Default 50.
        :return distances: (list) distancias
        
        """
        n_edges = len(self.edges)
        distances = [random.randint(rangeL, rangeR) for _ in range(n_edges)]
        return distances

    def createAdjMat(self):
        """
        Crea la matriz de adyacencia para un grafo 
        :return m: (numpy 2D-array) Matriz de adyacencia

        """
        distances = self.addDistances()
        n_dis = len(distances)
        n_nodes = len(self.nodes)
        edges = self.edges
        m = np.ones((n_nodes, n_nodes))*np.inf
        c = 0
        for e in edges:
            i = int(e.split("->")[0])
            j = int(e.split("->")[1])
            m[i, j] = distances[c]
            m[j, i] = distances[c]
            c += 1

        for i in range(m.shape[0]):
            for j in range(m.shape[1]):
                if i == j:
                    m[i, j] = 0
        return m

    def Dijkstra(self, s):
        """
        Regresa el árbol dado por el algoritmo Dijkstra de un grafo
        :param s: Nodo fuente
        :return dg: Dijkstra Tree (Graph)
        """
        #Crear árbol con objeto tipo Grafo y asignar tipo árbol
        dg = Graph()  
        dg.type = DIJKSTRA_TREE  
        dg.generator=self.type

        #Crear Matriz de Adyacencia 
        mat = self.createAdjMat() 

        INF = np.inf  # varible de valor infinito para representar nodos no vecinos
        
        distancias = [INF]*mat.shape[0]  # vector de distancias minimas
        
        visto = [False]*mat.shape[0]  # vector de nodos visitados
        padre = [-1]*mat.shape[0]  # nodos padres
        caminos = [()]*mat.shape[0]  # caminos
        
        # distancia de s a s is 0.
        distancias[s] = mat[s][s]  

        while sum(visto) < len(visto):
            dismin = INF  # dismin
            v_min = 0  # nodo con distancia minima
            for i in range(len(visto)):
                # obtener nodo de distancia minima
                if visto[i] == False and distancias[i] < dismin:
                    dismin = distancias[i]
                    v_min = i  # nodo de distancia minima

            visto[v_min] = True  # marca como visitado
            for i in range(len(visto)):  
                # si L(y) > L(x)+w(x,y)
                if not visto[i] and mat[v_min][i] != 0 and distancias[i] > distancias[v_min] + mat[v_min][i]:
                    # Actualizar distancia mínima
                    distancias[i] = distancias[v_min] + mat[v_min][i]
                    padre[i] = v_min  # Nodo padre del nodo i

        # Para caminos
        for i in range(len(padre)):
            nodo = i  # nodo final
            c = []
            while nodo != -1:  # hasta llegar al nodo inicio
                # Guardar nodo
                c.append(nodo)  

                # Se mueve al nodo predecesor
                nodo = padre[nodo]  
            caminos[i] = c[::-1]

        # Agregar edges al grafo dg (Graph)
        for camino in caminos:
            if len(camino) > 1:
                p = 0
                while p < len(camino)-1:
                    dg.addEdge(camino[p], camino[p+1],
                               f"{camino[p]}->{camino[p+1]}")
                    p += 1

        # Lista orden para guardar las distancias de cada nodo a s en gephi
        orden = []
        for camino in caminos:
            for r in camino:
                if r not in orden:
                    orden.append(r)

        # Se agregan las distancias a dg (Graph)
        for r in orden:
            dg.ds.append(distancias[r])

        return dg



    def KruskalD(self):
        """
        Regresa el árbol MST obtenido con el algoritmo de Kruskall D
        """

        #Crear árbol con objeto tipo Grafo y asignar tipo árbol
        kg = Graph()  
        kg.type = KRUSKALL_D  
        kg.generator=self.type


        distances = self.addDistances()
        vertex = list(self.edges.keys())
        sorted_vertex = []
        sorted_distances = []

        # vertex and distances ordered ascendently
        for _ in range(len(distances)):
            idx_min_distance = np.argmin(distances)
            sorted_vertex.append(vertex[idx_min_distance])
            sorted_distances.append(distances[idx_min_distance])
            vertex.pop(idx_min_distance)
            distances.pop(idx_min_distance)

        # Connected component
        connected_components = []
        for i in range(len(self.nodes)):
            temp = [False]*len(self.nodes)
            temp[i] = True
            connected_components.append(temp)
        # iteratee over all graph's vertex and check if their nodes don't belong
        # to the same subset to create edge in kruskal tree
        for i in range(len(sorted_vertex)):
            u = int(sorted_vertex[i].split('->')[0])
            v = int(sorted_vertex[i].split('->')[-1])

            # if u and v aren't in the same subset
            if connected_components[u] != connected_components[v]:
                kg.addEdge(u, v, f"{u}->{v}")
                for x in range(len(connected_components[u])):
                    if connected_components[u][x]:
                        for y in range(len(connected_components[v])):
                            if connected_components[v][y]:
                                connected_components[x][y] = True
                                connected_components[y][x] = True

                kg.mst += sorted_distances[i]

        return kg

    def KruskalI(self):
        """
        Regresa el árbol MST obtenido con el algoritmo de Kruskall I
        """
        #Crear árbol con objeto tipo Grafo y asignar tipo árbol
        kg = Graph()  
        kg.type = KRUSKALL_I  
        kg.generator=self.type
        
        distances = self.addDistances()
        vertex = list(self.edges.keys())
        sorted_vertex = []
        sorted_distances = []

        # vertex and distances ordered ascendently
        for _ in range(len(distances)):
            idx_min_distance = np.argmin(distances)
            sorted_vertex.append(vertex[idx_min_distance])
            sorted_distances.append(distances[idx_min_distance])
            vertex.pop(idx_min_distance)
            distances.pop(idx_min_distance)

        # Connected component
        connected_components = []
        for i in range(len(self.nodes)):
            temp = [False]*len(self.nodes)
            temp[i] = True
            connected_components.append(temp)
        # iteratee over all graph's vertex and check if their nodes don't belong
        # to the same subset to create edge in kruskal tree
        for i in range(len(sorted_vertex)):
            u = int(sorted_vertex[i].split('->')[0])
            v = int(sorted_vertex[i].split('->')[-1])

            # if u and v aren't in the same subset
            if connected_components[u] != connected_components[v]:
                kg.addEdge(u, v, f"{u}->{v}")
                for x in range(len(connected_components[u])):
                    if connected_components[u][x]:
                        for y in range(len(connected_components[v])):
                            if connected_components[v][y]:
                                connected_components[x][y] = True
                                connected_components[y][x] = True

                kg.mst += sorted_distances[i]

        return kg

    def Prim(self):
        """
        Regresa el árbol MST obtenido con el algoritmo de Prim
        """

        #Crear árbol con objeto tipo Grafo y asignar tipo árbol
        pg = Graph()  # Dijkstra graph
        pg.type = PRIM 
        pg.generator=self.type
        
        mat = self.createAdjMat()  # adjacent matrix mat
        INF = np.inf  # varible with infinite value to represent nodes no neighbors
        v = [0] * len(self.getNodes())
        n = len(v)
        s = np.random.choice(self.getNodes())
        v[s] = 1
        E = []
        for i in range(n-1):
            minimo = INF
            agregar_vertice = 0
            e = []
            for j in range(n):
                if v[j] == 1:
                    for k in range(n):
                        if v[k] == 0 and mat[j][k] < minimo:
                            agregar_vertice = k
                            e = [j, k]
                            minimo = mat[j][k]
            v[agregar_vertice] = 1
            pg.mst += minimo

            E.append(e)

        for edge in E:
            u = edge[0]
            v = edge[1]
            pg.addEdge(u, v, f"{u}->{v}")
        return pg